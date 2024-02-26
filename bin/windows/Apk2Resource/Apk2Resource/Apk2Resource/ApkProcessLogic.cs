using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Apk2Resource
{
    /// <summary>
    /// 封装apk 解包、打包、签名的简易调用逻辑
    /// </summary>
    public class ApkProcessLogic
    {
        public static string toolTipInfo = "请拖动待处理的游戏包至此";
        public static Boolean batchSign = false;                //批量签名
        public static List<String> Signs = new List<string>();  // 签名文件信息

        /// <summary>
        /// 载入签名文件信息
        /// </summary>
        public static void loadSigns(ComboBox comboBox_sign)
        {
            string preStr = comboBox_sign.Text;     //记录之前选中的信息
            comboBox_sign.Items.Clear();
            Signs.Clear();

            //所有签名文件
            string[] files = System.IO.Directory.GetFiles(SinPath());
            foreach (string file in files)
            {
                if (file.EndsWith(".pk8"))
                {
                    string name = System.IO.Path.GetFileNameWithoutExtension(file);
                    comboBox_sign.Items.Add(name);
                    Signs.Add(name);
                }
            }

            // 默认选中签名文件letang
            int index = comboBox_sign.Items.IndexOf(preStr.Equals("") ? "120" : preStr);
            if (index == -1 && comboBox_sign.Items.Count > 0) index = 0;
            if (index != -1) comboBox_sign.SelectedIndex = index;
        }

        /// <summary>
        /// 获取签名文件所在目录
        /// </summary>
        public static String SinPath()
        {
            return Apk2Resource.DependentFiles.toolsDir() + "signs";
        }

        public static void Form_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))    //判断拖来的是否是文件
                e.Effect = DragDropEffects.Link;                //是则将拖动源中的数据连接到控件
            else e.Effect = DragDropEffects.None;
        }

        public static void Form_DragDrop(object sender, DragEventArgs e)
        {
            TextBox textBox = sender as TextBox;
            String files = dragDrop(e);
            textBox.Text = files;
        }

        public static string dragDrop(DragEventArgs e)
        {
            StringBuilder filesName = new StringBuilder("");
            Array files = (System.Array)e.Data.GetData(DataFormats.FileDrop);//将拖来的数据转化为数组存储
            return ArrayToStr(files);
        }

        public static string ArrayToStr(Array files)
        {
            List<String> apkList = new List<string>();
            foreach (object iteam in files)
            {
                Dictionary<String, String> apk_dirs = getApk_FileOrDir(iteam.ToString());    // 获取目录下的apk文件或解压目录

                foreach (String apk in apk_dirs.Values.ToArray<String>())
                {
                    if (!apkList.Contains(apk)) apkList.Add(apk);
                }
            }

            return ToString(apkList);
        }

        // 转化Array为字符串形式
        private static String ToString(List<String> A)
        {
            String tmp = "";
            foreach (object iteam in A)
                tmp += ";" + iteam.ToString();

            tmp = tmp.Substring(1);
            return tmp;
        }

        /// <summary>
        /// 此函数用于实时显示cmd输出信息,在richTextBox1中显示输出信息
        /// </summary>
        public static void OutPut(String line)
        {
            Apk2Resource.Apktool.OutPut(line, RichBox, Form_m);
        }

        private static void richTextBox1_LinkClicked(object sender, LinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(e.LinkText);    //识别出超链接，点击后可以访问
        }

        #region apk解包并修改逻辑

        /// <summary>
        /// 执行apk修改逻辑, method为要执行的修改逻辑
        /// </summary>
        public static void Modify_Click(Form form, Button button, RichTextBox richBox, String sourceApks, String signName, Apk2Resource.Cmd.Method method = null)
        {
            Form_m = form;
            RichBox = richBox;
            SourceApks = sourceApks;
            SignName = signName;
            modifyMethod = method;
            //batchSign = signAll;

            //batchSign = true;
            Apk2Resource.Apktool.clearDirInfo();
            Apk2Resource.Cmd.ThreadRun(Modify_Logic, form, button, "执行中...");
        }

        private static string SourceApks = "";
        private static string SignName = "";
        private static RichTextBox RichBox;
        private static Form Form_m;
        private static Apk2Resource.Cmd.Method modifyMethod;

        public static String unpackPath = "";       // 记录apk解包后的文件路径

        /// <summary>
        /// apk解包、打包资源修改逻辑
        /// </summary>
        private static void Modify_Logic()
        {
            if (!SourceApks.Equals(toolTipInfo))
            {
                String[] apks = SourceApks.Split(';');
                Modify(apks, SignName, OutPut);
            }
            else OutPut("【E】" + "请先拖动待处理的游戏包至此工具上，再执行修改操作！");
        }

        /// <summary>
        /// 对给定的所有apk执行自打包修改
        /// </summary>
        public static void Modify(String[] apks, String sign, Apk2Resource.Cmd.Callback call)
        {
            int index = 0;
            foreach (String apk in apks)
            {
                if (call != null) call("【T】" + "-----------------------------------------------------------");
                if (call != null) call("【T】" + "处理第" + ++index + "个apk，共" + apks.Length + "个");
                if (call != null) call("【T】" + "-----------------------------------------------------------");


                

                //// 设置修改后的文件名称
                //String Dir = apk.Replace(".apk", "");

                //if (batchSign) Apk2Resource.Apktool.outputAPK_name = Dir.Substring(Dir.LastIndexOf("\\") + 1) + "_b.apk";
                //else Apk2Resource.Apktool.outputAPK_name = Dir.Substring(Dir.LastIndexOf("\\") + 1) + ".apk";

                //unpackPath = apkUnpack(apk, call);                         // apk解包

                // 根据apk路径生成解包路径
                string fileName = Path.GetFileNameWithoutExtension(apk).Replace("Ltsdk_", "").Replace("ltsdk_", "");
                string path = Path.GetDirectoryName(apk);
                string UnpackDestDir = path + "\\source配置_" + fileName + "\\combine\\" + fileName;

                unpackPath = apkUnpack(apk, call, true, UnpackDestDir);                         // apk解包


                //// 获取移动计费apk文件路径
                //String chargeApk = getChargeApk(unpackPath, call);
                //if (chargeApk.Equals("")) continue;
                //Modify_Process(chargeApk, unpackPath, call);            // 执行资源修改逻辑
                if (modifyMethod != null)
                {
                    call("【I】执行修改逻辑...");
                    modifyMethod();                                     // 执行指定的处理逻辑
                    call("【I】执行修改逻辑结束\r\n");
                }

                //String newAPK = apkPackage(unpackPath, sign, call);       // apk打包
            }
        }

        #endregion

        #region Apk解包、打包逻辑

        /// <summary>
        /// 执行apk修改逻辑, method为要执行的修改逻辑
        /// </summary>
        public static void PackUnpack_Click(Form form, Button button, RichTextBox richBox, String sourceApks, String signName, Apk2Resource.Cmd.Method method = null, bool signAll = false)
        {
            Form_m = form;
            RichBox = richBox;
            SourceApks = sourceApks;
            SignName = signName;
            modifyMethod = method;
            batchSign = signAll;

            //batchSign = true;
            Apk2Resource.Apktool.clearDirInfo();
            Apk2Resource.Cmd.ThreadRun(Modify_Logic, form, button, "执行中...");
        }

        #endregion

        //==========================
        // apk解包打包逻辑封装

        /// <summary>
        /// 若为apk文件，则先行解包
        /// </summary>
        public static String apkUnpack(String apkFile, Apk2Resource.Cmd.Callback call, bool deletPublicXML = false, string UnpackDestDir = "")
        {
            // 若输入的为apk文件，则自动进行解包
            if (Apk2Resource.Apktool.isApkFile(apkFile))
            {
                if (call != null) call("【I】" + Path.GetFileName(apkFile));
                if (call != null) call("【I】apk解包开始...");

                string dir = Apk2Resource.Apktool.unPackage(apkFile, call, deletPublicXML, UnpackDestDir.Equals(""), UnpackDestDir);   // 使用apktool进行apk的解包
                if (dir.Contains("【E】")) return dir;

                if (call != null) call("【I】apk解包结束！\r\n");
                return dir;
            }
            else return apkFile;
        }

        /// <summary>
        /// 执行apk打包逻辑
        /// </summary>
        public static String apkPackage(String apkUnPackageDir, String signFileName0, Apk2Resource.Cmd.Callback call)
        {
            // 重新打包apk,并签名
            if (call != null) call("【I】apk打包开始...");
            String result0 = Apk2Resource.Apktool.package(apkUnPackageDir, call);     // 使用apktool进行打包
            if (result0.Contains("【E】")) return result0;

            if (call != null) call("【I】apk未签名文件已生成！\r\n");


            String apkNAME = Apk2Resource.Apktool.outputAPK_name;

            List<String> signs = new List<String>();
            if (batchSign) signs = Signs;
            else signs.Add(signFileName0);

            String apkName = apkUnPackageDir + "..apk"; // 生成的未签名apk
            // 执行批量签名逻辑
            foreach (String signFileName in signs)
            {
                // 生成新的输出名
                int index = apkNAME.LastIndexOf(".apk");
                Apk2Resource.Apktool.outputAPK_name = apkNAME.Substring(0, index) + "_" + signFileName + ".apk";

                String result = result0;

                if (batchSign && call != null) call("【I】批量签名，执行中...");

                // 若有签名文件，则进行签名
                if (!signFileName.Equals(""))
                {
                    if (call != null) call("【I】apk签名中，" + signFileName + "...");

                    String pem = SinPath() + "\\" + signFileName + ".x509.pem";
                    String pk8 = SinPath() + "\\" + signFileName + ".pk8";
                    String psw = "letang123";
                    result = Apk2Resource.Apktool.Sign(apkName, pem, pk8, psw, call);
                    if (result.Contains("【E】")) return result;

                    if (call != null) call("【I】apk签名完成！\r\n");

                    //// 删除打包生成的未签名文件
                    //if (!batchSign && File.Exists(apkName)) File.Delete(apkName);
                }
            }

            if (File.Exists(apkName)) File.Delete(apkName);    // 删除打包生成的未签名文件

            if (call != null) call("【I】apk打包结束！\r\n");

            // 打包完成后清除缓存中的解包文件
            if (call != null) call("【I】清除缓存目录，" + apkUnPackageDir);
            Apk2Resource.Apktool.DeletDir(apkUnPackageDir);

            batchSign = false;

            return "";
        }


        //------------------------------------------------------------------------
        // 辅助功能函数

        /// <summary>
        /// 获取目录下，指定拓展名的所有文件名
        /// </summary>
        public static Dictionary<string, string> getFileNameByExt(string path, string extension)
        {
            Dictionary<string, string> dic = new Dictionary<string, string>();

            if (Directory.Exists(path))
            {
                //所有签名文件
                string[] files = Directory.GetFiles(path);
                foreach (string file in files)
                {
                    if (file.EndsWith(extension))
                    {
                        string name = System.IO.Path.GetFileName(file);
                        dic.Add(name, file);
                    }
                }
            }

            return dic;
        }

        /// <summary>
        /// 获取路径path下的所有apk文件，或apk解包根目录信息
        /// </summary>
        public static Dictionary<string, string> getApk_FileOrDir(String path)
        {
            Dictionary<string, string> FileDir = new Dictionary<string, string>();

            // 若载入的为apk文件
            if (Apk2Resource.Apktool.isApkDir(path) || Apk2Resource.Apktool.isApkFile(path))
            {
                string name = System.IO.Path.GetFileName(path);
                FileDir.Add(name, path);
            }
            else
            {
                Dictionary<string, string> apks = getFileNameByExt(path, ".apk");         // 获取所有apk文件信息
                Dictionary<string, string> apkDirs = getApkDir(path);                     // 获取所有apk解包路径信息

                // 优先添加apk文件的解包目录
                foreach (string dir in apkDirs.Keys)
                {
                    FileDir.Add(dir, apkDirs[dir]);
                }

                // 再添加没有解包目录的apk文件
                foreach (string apk in apks.Keys)
                {
                    String dir = apk.Replace(".apk", "").TrimEnd('.');
                    if (!apkDirs.Keys.Contains(dir)) FileDir.Add(apk, apks[apk]);
                }
            }

            return FileDir;
        }

        /// <summary>
        /// 获取path目录下的所有apk解包目录信息
        /// </summary>
        public static Dictionary<string, string> getApkDir(string path)
        {
            Dictionary<string, string> dic = new Dictionary<string, string>();

            if (Directory.Exists(path))
            {
                DirectoryInfo directoryInfo = new DirectoryInfo(path);
                DirectoryInfo[] dirs = directoryInfo.GetDirectories();
                foreach (DirectoryInfo dir in dirs)
                {
                    if (dir.Name.Equals("附加资源")) continue;    // 忽略附加资源目录

                    // 若为apk解包目录或文件，则直接添加
                    if (Apk2Resource.Apktool.isApkDir(dir.FullName))
                        dic.Add(dir.Name, dir.FullName);
                    // 若非apk解包目录，则检索其目录下的apk文件和子文件夹
                    else
                    {
                        Dictionary<string, string> listInner = getApk_FileOrDir(dir.FullName);
                        foreach (String subApk in listInner.Keys)
                        {
                            if (!dic.Keys.Contains(subApk)) dic.Add(subApk, listInner[subApk]);
                        }
                    }
                }
            }

            return dic;
        }

    }
}
