using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Apk2Resource
{
    /// <summary>
    /// 定义Apktool类，
    /// 调用Apktool.jar，对apk包进行解包、打包、签名 操作
    /// </summary>
    class Apktool
    {
        public static string ProcessTmp_dir = "";       // 工具缓存目录

        public static string outputAPK_dir = "";        // apk输出目录
        public static string outputAPK_name = "";       // apk输出名称

        public static string toolsDir = UpdateTool.NAMESPACE + "_tools";  // tools相关插件文件夹名称

        // 清除目录、名称信息
        public static void clearDirInfo()
        {
            ProcessTmp_dir = "";
            outputAPK_dir = "";
            outputAPK_name = "";
        }


        # region 工具基础功能函数

        // 判断是否为apk文件
        public static bool isApkFile(String file)
        {
            return System.IO.File.Exists(file) && file.EndsWith(".apk");
        }

        // 判断是否为apk文件解压后的文件目录
        public static bool isApkDir(String file)
        {
            return System.IO.Directory.Exists(file) && System.IO.File.Exists(file + "\\AndroidManifest.xml");
        }

        /// <summary>
        /// 为字符串str 添加双引号 add Double Quotation Marks
        /// </summary>
        private static String addDQM(String str)
        {
            return "\"" + str + "\"";
        }

        /// <summary>
        /// 删除指定文件目录，并重新创建
        /// </summary>
        public static String makeDir(String dir, bool useTimeMode = true)
        {
            String tmpDir = dir;                            // 生成新的路径
            if (useTimeMode) tmpDir = dir + "_@_" + DateTime.Now.ToString("yyyy_MM_dd_hh.mm.ss");

            if (System.IO.Directory.Exists(tmpDir))         // 若目标路径已存在,则删除
                Directory.Delete(tmpDir, true);
            System.IO.Directory.CreateDirectory(tmpDir);    // 创建缓存目录
            return tmpDir;
        }

        /// <summary>
        /// 使用apktool.jar执行命令
        /// 1、"d -f *.apk -o *\dir"  // 反编译*.apk到目录*\dir
        /// 2、"b *\dir -o *.apk"     // 编译*\dir目录为*.apk
        /// </summary>
        /// <param name="arg">apktool.jar 执行的命令</param>
        private static String ApktoolRun(String arg, Cmd.Callback call)
        {
            String apkTool = addDQM(System.AppDomain.CurrentDomain.BaseDirectory + toolsDir + "\\apktool.jar");
            //String javaExE = addDQM(System.AppDomain.CurrentDomain.BaseDirectory + toolsDir + "\\java.exe");
            String javaExE = "java";
            String cmdStr = javaExE + " -jar " + apkTool + " " + arg;

            return Cmd.Run(cmdStr, call);   // 调用cmd命令，运行apktool.jar
        }

        /// <summary>
        /// 使用signapk.jar执行命令
        /// 1、"*.x509.pem *.pk8 *1.apk *2.apk password"  // 使用签名文件，对*1.apk进行签名
        /// </summary>
        private static String SignApkRun(String arg, Cmd.Callback call)
        {
            String signTool = addDQM(System.AppDomain.CurrentDomain.BaseDirectory + toolsDir + "\\signapk.jar");
            //String javaExE = addDQM(System.AppDomain.CurrentDomain.BaseDirectory + toolsDir + "\\java.exe");
            String javaExE = "java";
            String cmdStr = javaExE + " -jar " + signTool + " " + arg;

            return Cmd.Run(cmdStr, call);   // 调用cmd命令，运行apktool.jar
        }

        /// <summary>
        /// 使用signapk.jar执行命令
        /// 1、"*.x509.pem *.pk8 *1.apk *2.apk password"  // 使用签名文件，对*1.apk进行签名
        /// </summary>
        private static String SignApkRun_keystore(String arg, Cmd.Callback call)
        {
            String signTool = addDQM(System.AppDomain.CurrentDomain.BaseDirectory + toolsDir + "\\signapk.jar");
            //String javaExE = addDQM(System.AppDomain.CurrentDomain.BaseDirectory + toolsDir + "\\java.exe");
            String javaExE = "java";
            String cmdStr = javaExE + " -jar " + signTool + " " + arg;

            return Cmd.Run(cmdStr, call);   // 调用cmd命令，运行apktool.jar
        }

        # endregion


        # region 封装的功能逻辑，解包、打包、签名

        /// <summary>
        /// apk解包（d:\*.apk）
        /// </summary>
        public static String unPackage(String apk, Cmd.Callback call, bool deletPublicXML = false, bool useTimeMode = true, string UnpackDestDir = "")
        {
            if (isApkFile(apk))
            {
                String unPackDir = apk;
                while (unPackDir.Contains("..")) unPackDir = unPackDir.Replace("..", ".");

                if (UnpackDestDir == null || UnpackDestDir.Equals(""))
                {
                    // 根据apk生成解包路径
                    if (ProcessTmp_dir.Equals("")) unPackDir = apk.Replace(".apk", "");
                    else unPackDir = ProcessTmp_dir + "\\" + Path.GetFileNameWithoutExtension(unPackDir);
                }
                else
                {
                    unPackDir = UnpackDestDir;
                }

                unPackDir = makeDir(unPackDir, useTimeMode);// 创建输出目录

                String unPack = "d -f " + addDQM(apk) + " -o " + addDQM(unPackDir); // 解包命令
                String result = ApktoolRun(unPack, call);   // 执行解包命令,实时信息输出到函数OutPut中
                unPackageDelet(unPackDir, deletPublicXML);  // 解包后删除非必须文件

                return result.Contains("【E】") ? result : unPackDir;
            }

            return "";
        }

        /// <summary>
        /// 删除解包后，非必须的文件
        /// </summary>
        private static void unPackageDelet(String unPackDir, bool deletPublicXML = false)
        {
            String dir = unPackDir + "\\original";
            if (System.IO.Directory.Exists(dir)) System.IO.Directory.Delete(dir, true);

            if (deletPublicXML)
            {
                String file = unPackDir + "\\res\\values\\public.xml";
                if (System.IO.File.Exists(file)) System.IO.File.Delete(file);
            }
        }

        /// <summary>
        /// 打包前自动清理apkTool.jar生成的缓存文件
        /// </summary>
        private static void ClearUserTmpApk()
        {
            try
            {
                String userName = System.Environment.UserName;
                String tmpApk = @"C:\Users\" + userName + @"\apktool\framework\1.apk";
                if (File.Exists(tmpApk)) File.Delete(tmpApk);
            }
            catch (Exception ex) { }
        }

        /// <summary>
        /// apk打包，对解包修改后的apk文件重新打包
        /// </summary>
        public static String package(String apkDir, Cmd.Callback call)
        {
            ClearUserTmpApk();

            if (isApkDir(apkDir))
            {
                // 设定输出apk文件名称
                String apkName = apkDir + "..apk";

                String packageCmd = "b " + addDQM(apkDir) + " -o " + addDQM(apkName); // 打包命令
                String result = ApktoolRun(packageCmd, call);                 // 执行打包命令,实时信息输出到函数OutPut中

                if (result.Contains("【E】") && Cmd.process9patchImage()) return package(apkDir, call);
                else return result.Contains("【E】") ? result : apkName;
            }
            return "";
        }

        /// <summary>
        /// 打包完成后，删除解包文件
        /// </summary>
        public static void DeletDir(String apkDir)
        {
            if (System.IO.Directory.Exists(apkDir)) System.IO.Directory.Delete(apkDir, true);
        }

        /// <summary>
        /// 打包完成后，删除指定的文件
        /// </summary>
        public static void DeletFile(String filePath)
        {
            if (File.Exists(filePath)) File.Delete(filePath);
        }

        /// <summary>
        /// apk签名，对打包后的apk文件重新签名,使用指定的pem、pk8和psw进行签名
        /// </summary>
        public static String Sign(String apk, String pem, String pk8, String psw, Cmd.Callback call)
        {
            if (isApkFile(apk))
            {
                String signedApk = apk.Replace(".apk", "..apk");

                String signCmd = addDQM(pem) + " " + addDQM(pk8) + " " + addDQM(apk) + " " + addDQM(signedApk) + " " + psw; // 签名命令
                String result = SignApkRun(signCmd, call);                 // 执行签名命令,实时信息输出到函数OutPut中
                if (result.Contains("【E】")) return result;

                // 设置apk输出名称
                String apkName = signedApk;
                if (!outputAPK_dir.Equals("")) apkName = outputAPK_dir + "\\" + Path.GetFileName(apkName);
                if (!outputAPK_name.Equals("")) apkName = Path.GetDirectoryName(apkName) + "\\" + outputAPK_name;

                if (!apkName.Equals(signedApk))
                {
                    if (File.Exists(apkName)) File.Delete(apkName);

                    String Dir = Path.GetDirectoryName(apkName);
                    if (Directory.Exists(Dir))
                    {
                        if (call != null) call("【I3】复制：" + signedApk + "到\r\n" + apkName);

                        File.Copy(signedApk, apkName);  // 复制生成的签名apk
                        File.Delete(signedApk);         // 删除原有签名apk
                        signedApk = apkName;            // 记录信息签名文件名称
                    }
                }

                // 在文件浏览器中显示生成的渠道计费包
                //Form4.ShowFileInExplorer(signedApk);

                return signedApk;
            }
            return "";
        }

        # endregion

        delegate void OutPut_Call(String line, RichTextBox textBox, Control root);


        # region 通用信息输出逻辑

        /// <summary>
        /// 此函数用于实时显示cmd输出信息, textBox为输出信息显示控件，root为textBox的根
        /// </summary>
        public static void OutPut(String line, RichTextBox textBox, Control root)
        {
            if (textBox == null) return;
            if (textBox.InvokeRequired)
            {
                OutPut_Call F = new OutPut_Call(OutPut);
                root.Invoke(F, new object[] { line, textBox, root });
            }
            else
            {
                if (line.StartsWith("jarfileName:")) return;     // 不输出签名信息

                // 超出RichTextBox最大容量时，自动清除
                if (textBox.TextLength + line.Length + 10 > textBox.MaxLength)
                    textBox.Text = "";

                line = replace(line);
                textBox.AppendText(Environment.NewLine);
                textBox.SelectionColor = getColor(line);
                textBox.AppendText(line);

                textBox.ScrollToCaret();
                textBox.Invalidate();

                //textBox1.Text += line + "\r\n";
            }
        }

        /// <summary>
        /// 替换输出信息的显示格式
        /// </summary>
        private static String replace(String str)
        {
            if (str.StartsWith("I:")) str = str.Replace("I:", "【I】");
            else if (str.StartsWith("jarfileName:")) str = "【I】" + str;
            return str;
        }

        /// <summary>
        /// 根据输出信息，设置显示颜色
        /// </summary>
        private static Color getColor(String str)
        {
            if (str.StartsWith("cmd>")) return Color.DarkBlue;
            else if (str.StartsWith("【I】")) return Color.Green;
            else if (str.StartsWith("【I2】")) return Color.RoyalBlue;
            else if (str.StartsWith("【I3】")) return Color.FromArgb(91, 186, 244);
            else if (str.StartsWith("【E】")) return Color.Red;
            else if (str.StartsWith("【E2】")) return Color.BlueViolet;
            else if (str.StartsWith("【E3】")) return Color.Purple;
            else if (str.StartsWith("【V】")) return Color.DarkSlateGray;
            else if (str.StartsWith("【L】")) return Color.FromArgb(57, 225, 126);
            else if (str.StartsWith("【T】")) return Color.FromArgb(102, 0, 51);
            else if (str.StartsWith("【W】")) return Color.FromArgb(202, 81, 0);
            else return Color.Black;
        }

        # endregion

    }

}
