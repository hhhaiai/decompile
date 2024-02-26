using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace Apk2Resource
{
    // 此类用于实现资源id的批量替换
    class ReplaceValues
    {
        //subDirs = getFile_List(rootDir, search, searchNum);

        // 所有文件或目录中的目标串信息
        //foreach (object iteam in listBox_search.Items)
        //{
        //    String source = iteam.ToString();
        //    ReplaceFileContent(source, replace_content, target);
        //}
        //MessageBox.Show("替换文件内容完成！");

        /// <summary>
        /// 获取rootDir目录下，文件内容包含name字段的所有文件, 检索包含containsNum个以上关键字的文件
        /// </summary>
        public static List<String> getFile_List(String rootDir, String name, int containsNum = 1)
        {
            List<String> Dirs = new List<string>();

            // 获取目录下的所有子目录
            List<String> subDirs = getSubDirNames(rootDir);
            foreach (String dirName in subDirs)
            {
                String subDir = rootDir + "\\" + dirName;
                List<String> list = getFile_List(subDir, name, containsNum);
                foreach (String Iteam in list) Dirs.Add(Iteam);
            }

            // 获取目录下的所有文件
            List<String> subFiles = getSubFileNames(rootDir);
            foreach (String fileName in subFiles)
            {
                String subFile = rootDir + "\\" + fileName;
                String content = fileToString(subFile);          // 获取文件内容

                if (content.Contains(name))
                {
                    if (containsNum == 1) Dirs.Add(subFile);   // 若文件内容中包含name
                    else if (Contains_Num(content, name) >= containsNum) Dirs.Add(subFile); // 或者含有指定数目及以上个name
                }
            }

            return Dirs;
        }


        // 获取dirPath下的子目录信息
        public static DirectoryInfo[] getDirectories(String dirPath)
        {
            DirectoryInfo directoryInfo = new DirectoryInfo(dirPath);
            return directoryInfo.GetDirectories();
        }

        // 获取dirPath下的子文件信息
        public static FileInfo[] getFiles(String dirPath)
        {
            DirectoryInfo directoryInfo = new DirectoryInfo(dirPath);
            return directoryInfo.GetFiles();
        }

        // 获取目录名称, 并忽略ingnore中指定的所有项
        public static List<String> DirNames(DirectoryInfo[] dirs, List<String> ingnore = null)
        {
            List<String> name = new List<string>();
            foreach (DirectoryInfo dir in dirs)
            {
                if (ingnore != null && ingnore.Contains(dir.Name)) continue;

                name.Add(dir.Name);
            }

            return name;
        }

        // 获取目录下的所有子目录信息
        public static List<String> getSubDirNames(String dirPath)
        {
            DirectoryInfo[] dirs = getDirectories(dirPath);
            List<String> name = new List<string>();

            if (dirs != null && dirs.Length > 0)
            {
                foreach (DirectoryInfo dir in dirs)
                    name.Add(dir.Name);
            }

            return name;
        }


        // 获取目录下的所有子文件信息
        public static List<String> getSubFileNames(String dirPath)
        {
            FileInfo[] files = getFiles(dirPath);
            List<String> name = new List<string>();

            if (files != null && files.Length > 0)
            {
                foreach (FileInfo file in files)
                    name.Add(file.Name);
            }

            return name;
        }


        /// <summary>
        /// 获取data中含有的subStr数目
        /// </summary>
        public static int Contains_Num(String data, String subStr)
        {
            int n = 0;
            String tmp = data;
            while (tmp.Contains(subStr))
            {
                n++;
                tmp = tmp.Substring(tmp.IndexOf(subStr) + subStr.Length);
            }

            return n;
        }

        /// <summary>
        /// 获取rootDir目录下，文件内容包含name字段的所有文件
        /// </summary>
        public static void ReplaceFileContent(String rootDir, String source, String target, Cmd.Callback call = null)
        {
            if (source.Equals(target)) return; // 原串与目标串相同则不需要替换

            if (File.Exists(rootDir))
            {
                String content = fileToString(rootDir);         // 获取文件内容
                if (content.Contains(source))                   // 替换为目标串
                {
                    content = content.Replace(source, target);
                    SaveProcess(content, rootDir);

                    if (call != null) call("【I】修改" + source + "->" + target + ",文件路径：" + rootDir);
                }
            }

            // 检测目录下文件并替换
            if (Directory.Exists(rootDir))
            {
                List<String> Dirs = getFile_List(rootDir, source);
                foreach (String dir in Dirs) ReplaceFileContent(dir, source, target, call);
            }
        }

        /// <summary>
        /// 获取文件中的数据串
        /// </summary>
        public static string fileToString(String filePath)
        {
            string str = "";

            //获取文件内容
            if (System.IO.File.Exists(filePath))
            {
                bool defaultEncoding = filePath.EndsWith(".txt");

                System.IO.StreamReader file1;

                file1 = new System.IO.StreamReader(filePath);                  //读取文件中的数据
                //if (defaultEncoding) file1 = new System.IO.StreamReader(filePath, Encoding.Default);//读取文件中的数据
                //else file1 = new System.IO.StreamReader(filePath);                  //读取文件中的数据

                str = file1.ReadToEnd();                                            //读取文件中的全部数据

                file1.Close();
                file1.Dispose();
            }
            return str;
        }

        /// <summary>
        /// 保存数据data到文件处理过程，返回值为保存的文件名
        /// </summary>
        public static String SaveProcess(String data, String filePath, bool replace = false)
        {
            //不存在该文件时先创建
            System.IO.StreamWriter file1 = new System.IO.StreamWriter(filePath, !replace/*, System.Text.Encoding.UTF8*/);     //文件已覆盖方式添加内容

            file1.Write(data);                                                              //保存数据到文件

            file1.Close();                                                                  //关闭文件
            file1.Dispose();                                                                //释放对象

            return filePath;
        }


        #region 检索文件名称

        /// <summary>
        /// 获取rootDir目录下，所有包含name字段的子目录
        /// </summary>
        public static List<String> getDir_List(String rootDir, String name)
        {
            List<String> Dirs = new List<string>();

            // 获取目录下的所有子目录
            List<String> subDirs = getSubDirNames(rootDir);
            foreach (String dirName in subDirs)
            {
                String subDir = rootDir + "\\" + dirName;
                if (dirName.Contains(name)) Dirs.Add(subDir);
                else
                {
                    List<String> list = getDir_List(subDir, name);
                    foreach (String Iteam in list) Dirs.Add(Iteam);
                }
            }

            // 获取目录下的所有文件
            List<String> subFiles = getSubFileNames(rootDir);
            foreach (String fileName in subFiles)
            {
                String subDir = rootDir + "\\" + fileName;
                if (fileName.Contains(name)) Dirs.Add(subDir);
            }

            // 解析子字段对应的文件或目录信息
            if (name.Contains("|"))
            {
                String[] names = name.Split('|');
                List<String> list = getDir_List(rootDir, names);
                Dirs = listAdd(Dirs, list);
            }

            return Dirs;
        }

        /// <summary>
        /// 一次检测多个name对应的文件或目录信息
        /// </summary>
        public static List<String> getDir_List(String rootDir, String[] names)
        {
            List<String> Dirs = new List<string>();
            foreach (String name in names)
            {
                List<String> list = getDir_List(rootDir, name);
                Dirs = listAdd(Dirs, list);
            }
            return Dirs;
        }

        /// <summary>
        /// 合并list1和list2到新的list
        /// </summary>
        private static List<String> listAdd(List<String> list1, List<String> list2)
        {
            List<String> list = new List<string>();
            foreach (String iteam in list1) if (!list.Contains(iteam)) list.Add(iteam);
            foreach (String iteam in list2) if (!list.Contains(iteam)) list.Add(iteam);
            return list;
        }

        #endregion

    }
}
