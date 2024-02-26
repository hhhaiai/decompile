
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Apk2Resource
{
    public class FileProcess
    {
        #region 文件读取与保存

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
        public static String SaveProcess(String data, String filePath, Encoding encoding = null)
        {
            //不存在该文件时先创建
            System.IO.StreamWriter file1 = null;
            if (encoding == null) file1 = new System.IO.StreamWriter(filePath, false/*, System.Text.Encoding.UTF8*/);     //文件已覆盖方式添加内容
            else file1 = new System.IO.StreamWriter(filePath, false, Encoding.Default);     // 使用指定的格式进行保存

            file1.Write(data);                                                              //保存数据到文件

            file1.Close();                                                                  //关闭文件
            file1.Dispose();                                                                //释放对象

            return filePath;
        }

        /// <summary>
        /// 获取当前运行目录
        /// </summary>
        public static string CurDir()
        {
            return AppDomain.CurrentDomain.BaseDirectory;
        }

        #endregion
    }
}