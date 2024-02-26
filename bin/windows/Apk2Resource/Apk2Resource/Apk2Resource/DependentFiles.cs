
using Apk2Resource.Properties;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Apk2Resource
{
    class DependentFiles
    {
        /// <summary>
        /// 获取当前运行路径
        /// </summary>
        public static string curDir()
        {
            return AppDomain.CurrentDomain.BaseDirectory;
        }

        /// <summary>
        /// 获取当前运行路径下的tools目录
        /// </summary>
        public static string toolsDir()
        {
            return AppDomain.CurrentDomain.BaseDirectory + Apk2Resource.Apktool.toolsDir + "\\";
        }

        /// <summary>
        /// 获取当前运行路径下的tools目录
        /// </summary>
        public static string modifyResDir()
        {
            return AppDomain.CurrentDomain.BaseDirectory + Apk2Resource.Apktool.toolsDir + "\\modifyRes\\";
        }

        /// <summary>
        /// 检测目录是否存在，若不存在则创建
        /// </summary>
        public static void checkDir(string path)
        {
            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }
        }

        /// <summary>
        /// 保存Byte数组为文件
        /// </summary>
        public static void SaveFile(Byte[] array, string path, bool repalce = false)
        {
            if (repalce && System.IO.File.Exists(path)) System.IO.File.Delete(path);    // 若目标文件存在，则替换
            if (!System.IO.File.Exists(path))
            {
                // 创建输出路径
                String dir = System.IO.Path.GetDirectoryName(path);
                checkDir(dir);

                // 创建输出流
                System.IO.FileStream fs = new System.IO.FileStream(path, System.IO.FileMode.Create);

                //将byte数组写入文件中
                fs.Write(array, 0, array.Length);
                fs.Close();
            }
        }

        //=============================================

        /// <summary>
        /// 检测所有依赖文件，没有则生成
        /// </summary>
        public static void checksAll()
        {
            //check("apktool");
            check("signapk");
            check("signer");
            check("zipalign");
            //check("Update");
            //check("LogConfig");
            //check("AdIdConfig");
            //check("AdVisibleIds");
            //check("AdUnVisibleIds");
            check("java.exe");
            check("get_Manifest_txt.exe");
            checkSigns();
            //checkModifyRes();
        }

        /// <summary>
        /// 检测文件是否存在，不存在则创建
        /// </summary>
        public static void check(string name)
        {
            string tools = curDir() + Apk2Resource.Apktool.toolsDir;
            checkDir(tools);
            tools += "\\";

            //if (name.Equals("apktool")) SaveFile(Resources.apktool, tools + "apktool.jar");
            //else 
            if (name.Equals("signapk")) SaveFile(Resources.signapk, tools + "signapk.jar");
            else if (name.Equals("signer")) SaveFile(Resources.signer, tools + "signer.jar");
            else if (name.Equals("zipalign")) SaveFile(Resources.zipalign, tools + "zipalign.exe");
            //else if (name.Equals("Update")) SaveFile(Resources.UpdateFiles, tools + "UpdateFiles.exe", true);
            //else if (name.Equals("LogConfig")) SaveFile(Resources.LogConfig, tools + "LogConfig.txt");
            //else if (name.Equals("AdIdConfig")) SaveFile(Resources.AdIdConfig, tools + "AdIdConfig.txt");
            //else if (name.Equals("AdVisibleIds")) SaveFile(Resources.AdVisibleIds, tools + "AdVisibleIds.txt");
            //else if (name.Equals("AdUnVisibleIds")) SaveFile(Resources.AdUnVisibleIds, tools + "AdUnVisibleIds.txt");
            else if (name.Equals("java.exe")) SaveFile(Resources.java, tools + "java.exe");
            else if (name.Equals("get_Manifest_txt.exe")) SaveFile(Resources.get_Manifest_txt, tools + "get_Manifest_txt.exe");
        }

        /// <summary>
        /// 检查签名是否存在，不存在则创建
        /// </summary>
        public static void checkSigns()
        {
            string signs = curDir() + "\\" + Apk2Resource.Apktool.toolsDir + "\\signs";
            checkDir(signs);
            signs += "\\";

            SaveFile(Resources._120, signs + "120.pk8");
            SaveFile(Resources._120_x509, signs + "120.x509.pem");
            SaveFile(Resources.letang, signs + "letang.pk8");
            SaveFile(Resources.letang_x509, signs + "letang.x509.pem");
        }

        ///// <summary>
        ///// 检查修改工具的资源文件，不存在则创建
        ///// </summary>
        //public static void checkModifyRes()
        //{
        //    string modifyRes = curDir() + "\\" + Apk2Resource.Apktool.toolsDir + "\\modifyRes";
        //    checkDir(modifyRes);
        //    modifyRes += "\\";

        //    SaveFile(Resources.OneUtil4Perpre_cmd, modifyRes + "OneUtil4Perpre_cmd.jar");
        //    SaveFile(Resources.libperpre, modifyRes + "libperpre.so", true);
        //    SaveFile(Resources.OneUtil4Modis, modifyRes + "OneUtil4Modis.smali", true);
        //    SaveFile(Resources.PaymentCUApplication, modifyRes + "PaymentCUApplication.smali", true);
        //}


        /// <summary>
        /// 为arg添加引号
        /// </summary>
        private static string AddQuotation(string arg)
        {
            if (arg.EndsWith("\\") && !arg.EndsWith("\\\\")) arg += "\\";
            arg = "\"" + arg + "\"";

            return arg;
        }

        /// <summary>
        /// 使用OneUtil4Perpre_cmd.jar执行命令
        /// set oldname=%1
        /// set newname=%oldname:.apk=%
        /// java -jar %~dp0OneUtil4Perpre_cmd.jar "%oldname%" "%newname%"
        /// 
        /// 从给定的apk文件apkPath在路径desDir下生成perpre.dat
        /// </summary>
        public static String genPerpre_dat(String apkPath, String desDir, Cmd.Callback call)
        {
            String preperTool = AddQuotation(modifyResDir() + "OneUtil4Perpre_cmd.jar");
            String arg = AddQuotation(apkPath) + " " + AddQuotation(desDir);
            String cmdStr = "java -jar " + preperTool + " " + arg;

            return Cmd.Run(cmdStr, call);   // 调用cmd命令，运行apktool.jar
        }

    }
}
