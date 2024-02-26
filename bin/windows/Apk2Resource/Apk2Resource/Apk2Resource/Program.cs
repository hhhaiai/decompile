using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Apk2Resource
{
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main(String[] args)
        {
            //args = new String[] { @"G:\sc\桌面快捷存储\其他\20190218\ltsdk_18_v2.6.7_lenovo.apk" };

            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            UpdateTool.AutoUpdate();                    // 应用自动检测更新
            Apk2Resource.DependentFiles.checksAll();    // 检测工具运行依赖文件

            if (args != null && args.Length > 0)
            {
                string files = ApkProcessLogic.ArrayToStr(args);
                MainFrom.Apk2ResourceLogic(files);      // 执行apk修改逻辑
            }
            else
            {
                Application.Run(new MainFrom());        // 显示修改工具主界面
            }

        }
    }
}
