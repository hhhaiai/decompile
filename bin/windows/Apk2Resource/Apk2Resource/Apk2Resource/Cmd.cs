using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Apk2Resource
{
    /// <summary>
    /// 执行CMD命令，或以进程的形式打开应用程序（d:\*.exe）
    /// </summary>
    public class Cmd
    {
        public static bool useBatMode = false;  // 是否使用.bat模式运行工具
        public static bool singleBat = true;    // 是否使用单个bat文件执行操作


        /// <summary>
        /// 定义委托接口处理函数，用于实时处理cmd输出信息，或传递功能逻辑变量
        /// </summary>
        public delegate void Method();

        /// <summary>
        /// 在新的线程中执行method逻辑
        /// </summary>
        public static void ThreadRun(Method method, Form form = null, Button button = null, String Text = "执行中", bool useThread = true)
        {
            if (useThread)
            {
                Thread thread = new Thread(delegate()
                    {
                        // 允许不同线程间的调用
                        Control.CheckForIllegalCrossThreadCalls = false;

                        // 设置按钮和界面按钮不可用
                        String text = "";
                        if (form != null) form.ControlBox = false;

                        if (button != null)
                        {
                            text = button.Text;
                            button.Text = Text;
                            button.Enabled = false;
                        }

                        // 执行method逻辑
                        if (method != null) method();


                        if (button != null)
                        {
                            button.Text = text;
                            button.Enabled = true;
                        }
                        if (form != null) form.ControlBox = true;
                    });

                thread.Priority = ThreadPriority.AboveNormal;           // 设置子线程优先级
                Thread.CurrentThread.Priority = ThreadPriority.Highest; // 设置当前线程为最高优先级
                thread.Start();
            }
            else
            {
                // 设置按钮和界面按钮不可用
                String text = "";
                if (form != null) form.ControlBox = false;

                if (button != null)
                {
                    text = button.Text;
                    button.Text = Text;
                    button.Enabled = false;
                }

                // 执行method逻辑
                if (method != null) method();


                if (button != null)
                {
                    button.Text = text;
                    button.Enabled = true;
                }
                if (form != null) form.ControlBox = true;
            }
        }

        /// <summary>
        /// 以后台进程的形式执行应用程序（d:\*.exe）
        /// </summary>
        public static Process newProcess(String exe)
        {
            Process P = new Process();
            P.StartInfo.CreateNoWindow = true;
            P.StartInfo.FileName = exe;
            P.StartInfo.UseShellExecute = false;
            P.StartInfo.RedirectStandardError = true;
            P.StartInfo.RedirectStandardInput = true;
            P.StartInfo.RedirectStandardOutput = true;
            //P.StartInfo.WorkingDirectory = @"C:\windows\system32";
            P.Start();
            return P;
        }

        /// <summary>
        /// 创建指定命令的bat文件
        /// </summary>
        public static string createTmpBat(String cmd)
        {
            String filePath = DependentFiles.toolsDir() + (singleBat ? "CMD_FILE" : DateTime.Now.Ticks.ToString()) + ".bat";
            FileProcess.SaveProcess(cmd, filePath, Encoding.Default);

            return filePath;
        }

        /// <summary>
        /// 创建包含cmd命令的.bat文件，并执行
        /// </summary>
        public static string Run_bat(string cmd)
        {
            String bat = createTmpBat(cmd);

            Process P = newProcess(bat);
            string outStr = P.StandardOutput.ReadToEnd();
            P.Close();

            if (File.Exists(bat)) File.Delete(bat);
            return outStr;
        }

        /// <summary>
        /// 执行CMD命令
        /// </summary>
        public static string Run(string cmd, bool useBatMode = true)
        {
            if (useBatMode) return Run_bat(cmd);    // 使用.bat文件模式执行cmd命令
            else
            {
                Process P = newProcess("cmd.exe");
                P.StandardInput.WriteLine(cmd);
                P.StandardInput.WriteLine("exit");
                string outStr = P.StandardOutput.ReadToEnd();
                P.Close();
                return outStr;
            }
        }

        /// <summary>
        /// 定义委托接口处理函数，用于实时处理cmd输出信息
        /// </summary>
        public delegate void Callback(String line);

        ///// <summary>
        ///// 此函数用于实时显示cmd输出信息, Callback示例
        ///// </summary>
        //private void Callback1(String line)
        //{
        //    textBox1.AppendText(line);
        //    textBox1.AppendText(Environment.NewLine);
        //    textBox1.ScrollToCaret();

        //    richTextBox1.SelectionColor = Color.Green;
        //    richTextBox1.AppendText(line);
        //    richTextBox1.AppendText(Environment.NewLine);
        //    richTextBox1.ScrollToCaret();
        //}

        private static string outStr = "";
        private static Callback DataReceivedCall;
        private static void processOutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            string baseDir = System.AppDomain.CurrentDomain.BaseDirectory.TrimEnd('\\');
            List<string> lines = new List<string>();

            try
            {
                string line = e.Data;
                checkOutLines(line);

                // cmd运行输出信息
                if (line != null && !line.Equals("") && !line.EndsWith(">exit"))
                {
                    if (line.StartsWith(baseDir + ">")) line = line.Replace(baseDir + ">", "cmd>\r\n"); // 识别的cmd命令行信息
                    line = ((line.Contains("[Fatal Error]") || line.Contains("ERROR:") || line.Contains("Exception")) ? "【E】 " : "") + line;
                    if (DataReceivedCall != null) DataReceivedCall(line);
                    outStr += line + "\r\n";
                }
            }
            catch (Exception ex)
            {
                //MessageBox.Show(ex.ToString() + " e=" + e.ToString());
            }
        }

        private static List<string> List9patchImage = new List<string>();
        private static void checkOutLines(string line)
        {
            try
            {
                string startKey = "ERROR: 9-patch image", endKey = "malformed.";
                if (line.Contains(startKey) && line.Contains(endKey))
                {
                    int start = line.IndexOf(startKey) + startKey.Length;
                    int end = line.LastIndexOf(endKey);
                    string imagePath = line.Substring(start, end - start).Trim();

                    if (!imagePath.Equals("") && !List9patchImage.Contains(imagePath))
                        List9patchImage.Add(imagePath);
                }
            }
            catch (Exception ex)
            {
                //MessageBox.Show(ex.ToString() + " ex=" + ex.ToString());
            }
        }

        //判定是否执行了9patchImage修改逻辑
        public static bool process9patchImage()
        {
            if (List9patchImage.Count > 0)
            {
                if (DataReceivedCall != null) DataReceivedCall("【I】 执行了9patchImage修改逻辑:(修改.png -> .jpg)");

                foreach (string path in List9patchImage)
                {
                    // 修改.png -> .jpg 或 .jpg -> .png
                    string targetPath = path.Substring(0, path.LastIndexOf(".")) + (path.ToLower().EndsWith(".png") ? ".jpg" : ".png");
                    if (File.Exists(path)) File.Move(path, targetPath);

                    if (DataReceivedCall != null) DataReceivedCall("【I】 修改文件，" + path);
                }

                List9patchImage.Clear();
                return true;
            }

            return false;
        }

        /// <summary>
        /// 执行CMD语句,实时获取cmd输出结果，输出到call函数中
        /// </summary>
        /// <param name="cmd">要执行的CMD命令</param>
        public static string Run(string cmd, Callback call/*, bool useBatMode = true*/)
        {
            //string cmd_exe = DependentFiles.curDir() + "tools\\cmd.exe";

            String CMD_FILE = useBatMode ? createTmpBat(cmd) : "cmd.exe"; // 使用.bat文件模式执行cmd命令

            Process P = newProcess(CMD_FILE);
            if (!useBatMode)
            {
                P.StandardInput.WriteLine(cmd);
                P.StandardInput.WriteLine("exit");
            }

            DataReceivedCall = call;
            P.OutputDataReceived += new DataReceivedEventHandler(processOutputDataReceived);    // 输出运行信息
            P.ErrorDataReceived += new DataReceivedEventHandler(processOutputDataReceived);     // 输出报错信息

            P.BeginOutputReadLine();
            P.BeginErrorReadLine();

            outStr = "";

            P.WaitForExit();
            P.Close();

            // 使用bat模式，非单个bat，执行逻辑后删除bat文件
            if (useBatMode && !singleBat && File.Exists(CMD_FILE)) File.Delete(CMD_FILE);

            return outStr;
        }


        /// <summary>
        /// 以进程的形式打开应用程序（d:\*.exe）,并执行命令
        /// </summary>
        public static void RunProgram(string programName, string cmd)
        {
            Process P = newProcess(programName);
            if (cmd.Length != 0)
            {
                P.StandardInput.WriteLine(cmd);
            }
            P.Close();
        }


        /// <summary>
        /// 正常启动window应用程序（d:\*.exe）
        /// </summary>
        public static void Open(String exe)
        {
            System.Diagnostics.Process.Start(exe);
        }

        /// <summary>
        /// 正常启动window应用程序（d:\*.exe）,并传递初始命令参数
        /// </summary>
        public static void Open(String exe, String args)
        {
            System.Diagnostics.Process.Start(exe, args);
        }
    }

}
