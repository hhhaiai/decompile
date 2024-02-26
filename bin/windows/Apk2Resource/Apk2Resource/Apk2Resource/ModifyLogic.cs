using Apk2Resource.Properties;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Apk2Resource
{
    class ModifyUnpakDir
    {
        public static void Modify(String UnpackPath)
        {
            //ApkProcessLogic.OutPut(info);
            string Name = UnpackPath.Substring(UnpackPath.LastIndexOf("\\") + 1);
            string sourceDir = UnpackPath.Substring(0, UnpackPath.LastIndexOf("\\combine\\"));

            DeletDir(UnpackPath, "original");
            DeletFile(UnpackPath, "apktool.yml");

            CopyFile(UnpackPath + "\\AndroidManifest.xml", sourceDir + "\\" + Name + "_AndroidManifest.txt");
            RenameFile(UnpackPath, "AndroidManifest.xml", "manifest.txt");
            ProcessManfest(UnpackPath);

            MoveDir(UnpackPath + "\\assets\\ltsdk_res", sourceDir + "\\configure\\1002\\" + Name + "\\assets\\ltsdk_res");
            RenameValues(UnpackPath);

            DeletDir(UnpackPath, "smali\\com\\unity3d");
            DeletDir(UnpackPath, "smali\\org\\fmod");
        }

        private static bool ManActivityIsConfiged(string configPath)
        {
            string configData = FileProcess.fileToString(configPath).Replace("\r\n", "\n");
            string[] A = configData.Split('\n');
            foreach(string a in A)
            {
                if (a.Trim().StartsWith("GameEntryActivity=")) return true;
            }
            return false;
        }

        /// <summary>
        /// Manifest文件格式处理
        /// </summary>
        private static void ProcessManfest(String UnpackPath)
        {
            bool keepLanchActivity = ManActivityIsConfiged(UnpackPath + "\\assets\\ltsdk_res\\config.txt");

            String apkTool = addDQM(System.AppDomain.CurrentDomain.BaseDirectory + Apktool.toolsDir + "\\get_Manifest_txt.exe");
            string arguments = addDQM(UnpackPath + "\\manifest.txt");
            if (keepLanchActivity) arguments = arguments + " " + "KeepLancherActivity";
            //string cmd = apkTool + " " + manifest;
            System.Diagnostics.Process.Start(apkTool, arguments);
        }

        private static void RenameValues(String UnpackPath)
        {
            string resDir = UnpackPath + "\\res";

            ApkProcessLogic.OutPut("【I】---------------------------");
            ApkProcessLogic.OutPut("【I】重命名" + resDir + "\\value目录下所有文件");

            if (Directory.Exists(resDir))
            {
                DirectoryInfo dir = new DirectoryInfo(resDir);
                DirectoryInfo[] valueDirs = dir.GetDirectories();

                foreach(DirectoryInfo value in valueDirs)
                {
                    string name = value.Name;
                    if(name.Equals("values") || name.StartsWith("values-"))
                    {
                        RenameSubFiles(value, "ltsdk_");
                    }
                }
            }
        }

        private static void RenameSubFiles(DirectoryInfo value, string startAppend)
        {
            FileInfo[] fileInfos = value.GetFiles();
            foreach(FileInfo fileInfo in fileInfos)
            {
                ApkProcessLogic.OutPut("【I】" + fileInfo.DirectoryName + "\\" + fileInfo.Name + " 重命名为：" + startAppend + fileInfo.Name);
                string preName = fileInfo.DirectoryName + "\\" + fileInfo.Name;
                string newName = fileInfo.DirectoryName + "\\" + startAppend + fileInfo.Name;
                File.Move(preName, newName);
            }
        }

        /// <summary>
        /// 为字符串str 添加双引号 add Double Quotation Marks
        /// </summary>
        private static String addDQM(String str)
        {
            return "\"" + str + "\"";
        }

        public static void DeletDir(string UnpackPath, string relativePath)
        {
            String dir = UnpackPath + "\\" + relativePath;
            if (Directory.Exists(dir))
            {
                ApkProcessLogic.OutPut("【I】---------------------------");
                ApkProcessLogic.OutPut("【I】删除" + relativePath + "所在目录 " + dir);

                Directory.Delete(dir, true);
            }
            
        }

        public static void DeletFile(string UnpackPath, string relativePath)
        {
            String file = UnpackPath + "\\" + relativePath;
            if (File.Exists(file))
            {
                ApkProcessLogic.OutPut("【I】---------------------------");
                ApkProcessLogic.OutPut("【I】删除" + relativePath);

                File.Delete(file);
            }
        }

        public static void RenameFile(string UnpackPath, string relativePath, string newRelativePath)
        {
            String file = UnpackPath + "\\" + relativePath;
            String newfile = UnpackPath + "\\" + newRelativePath;

            if (File.Exists(newfile)) File.Delete(newfile);
            if (File.Exists(file))
            {
                ApkProcessLogic.OutPut("【I】---------------------------");
                ApkProcessLogic.OutPut("【I】重命名AndroidManifest.xml为manifest.txt");

                File.Move(file, newfile);
            }
        }

        public static void checkDir(string destDir)
        {
            if (!Directory.Exists(destDir)) Directory.CreateDirectory(destDir);
        }

        public static void CopyFile(string source, string dest)
        {
            if (File.Exists(dest)) File.Delete(dest);
            string destDir = Path.GetDirectoryName(dest);
            checkDir(destDir);

            if (File.Exists(source))
            {
                ApkProcessLogic.OutPut("【I】---------------------------");
                ApkProcessLogic.OutPut("【I】复制文件" + source + " -> " + dest);

                File.Copy(source, dest, true );
            }
        }
        public static void MoveDir(string source, string dest)
        {
            if (File.Exists(dest)) Directory.Delete(dest, true);
            string destParentDir = dest.Substring(0, dest.LastIndexOf("\\"));
            checkDir(destParentDir);

            if (Directory.Exists(source))
            {
                ApkProcessLogic.OutPut("【I】---------------------------");
                ApkProcessLogic.OutPut("【I】移动目录" + source + " -> " + dest);

                Directory.Move(source, dest);
            }
        }
    }

    //class ModifySmali
    //{

    //    //.method public bridge synthetic setAdUnitId(Ljava/lang/String;)V
    //    //    .locals 0
    //    //    invoke-super {p0, p1}, Lcom/google/android/gms/ads/BaseAdView;->setAdUnitId(Ljava/lang/String;)V
    //    //    return-void
    //    //.end method

    //    /// <summary>
    //    /// 获取smali文件中指定名称的method
    //    /// </summary>
    //    public static String getMethod(String smaliData, String method)
    //    {
    //        String str = "";
    //        String methodKey = " " + method + "(";

    //        if (!smaliData.Equals("") && smaliData.Contains(methodKey))
    //        {
    //            String[] A = Tools.SplitTwo(smaliData, methodKey, false);
    //            if (A[0].Contains(".method") && A[1].Contains(".end method"))
    //            {
    //                int start = A[0].LastIndexOf(".method");
    //                int end = A[0].Length + methodKey.Length + A[1].IndexOf(".end method") + ".end method".Length;

    //                str = smaliData.Substring(start, end - start);
    //            }
    //        }

    //        return str;
    //    }

    //    /// <summary>
    //    /// 获取method方法逻辑开始位置索引
    //    /// </summary>
    //    public static int getMethodLogicIndex(String methodContent)
    //    {
    //        methodContent = methodContent.Replace(".line", "$line");// 替换所有".line标记"，避免其中的“.”号位置干扰
    //        methodContent = methodContent.Replace("..", "$$");      // 替换所有"..标记"，避免其中的“.”号位置干扰

    //        int index = methodContent.LastIndexOf("return");        // return索引位置
    //        if (index != -1)
    //        {
    //            String str = methodContent.Substring(0, index);     // 获取return前的串
    //            index = str.LastIndexOf(".");                       // 获取最后一个“.”的索引位置
    //            index = str.IndexOf("\n", index) + "\n".Length;     // 获取“.”之后的第一个换行符位置
    //        }

    //        return index;
    //    }

    //    /// <summary>
    //    /// 判断方法是否为静态方法
    //    /// .method public static handleFullscreenDestroy()V
    //    /// </summary>
    //    public static bool isStatic(String methodContent)
    //    {
    //        bool b = false;
    //        if (methodContent.Contains(".method") && methodContent.Contains("("))
    //        {
    //            int start = methodContent.IndexOf(".method") + ".method".Length;
    //            int end = methodContent.IndexOf("(");
    //            String headStr = methodContent.Substring(start, end - start);   // 获取子串 public static handleFullscreenDestroy

    //            if (headStr.Contains(" static ")) b = true;                     // 是否为静态方法
    //        }
    //        return b;
    //    }

    //    /// <summary>
    //    /// 获取method方法内部变量数量
    //    /// </summary>
    //    public static int getLocals(String methodContent)
    //    {
    //        //.locals 0
    //        int Num = 0;
    //        if (methodContent.Contains(".locals"))
    //        {
    //            int start = methodContent.IndexOf(".locals") + ".locals".Length;
    //            int end = methodContent.IndexOf('\n', start);

    //            String data = methodContent.Substring(start, end - start).Trim();
    //            Num = Int32.Parse(data);
    //        }
    //        return Num;
    //    }


    //    /// <summary>
    //    /// 获取method方法内部cond标记最大值
    //    /// </summary>
    //    public static int getCond(String methodContent)
    //    {
    //        //:cond_0
    //        int Num = -1;
    //        while(methodContent.Contains(":cond_"))
    //        {
    //            int start = methodContent.IndexOf(":cond_") + ":cond_".Length;
    //            int end = methodContent.IndexOf('\n', start);

    //            String data = methodContent.Substring(start, end - start).Trim();
    //            int n = ToInt(data);            // 获取cond_值
    //            String HexN = ToHex(n); 

    //            if (n > Num) Num = n;           // 记录最大值
    //            methodContent = methodContent.Replace(":cond_" + HexN, "XXX_" + HexN);    // 移除已修改
    //        }
    //        return Num;
    //    }

    //    /// <summary>
    //    /// 转化16进制串为整数
    //    /// </summary>
    //    public static int ToInt(String hex)
    //    {
    //        int num = 0;
    //        foreach(char C in hex.ToCharArray())
    //        {
    //            num = num * 16 + toInt(C);
    //        }

    //        return num;
    //    }

    //    /// <summary>
    //    /// 转化Num为16进制串
    //    /// </summary>
    //    public static String ToHex(int Num)
    //    {
    //        String str = "";
    //        while (Num >= 0)
    //        {
    //            int M = Num % 16;   // 取余数
    //            char C = toHex(M);  // 转化为16进制串
    //            str = C + str;
    //            Num = Num / 16;     // 取整
    //            if (Num == 0) break;
    //        }
    //        return str;
    //    }

    //    /// <summary>
    //    /// 转化char为整数
    //    /// </summary>
    //    private static int toInt(char hex)
    //    {
    //        if ('a' <= hex && hex <= 'z') return hex - 'a' + 10;
    //        else if ('A' <= hex && hex <= 'Z') return hex - 'A' + 10;
    //        else if ('0' <= hex && hex <= '9') return hex - '0';
    //        else return 0;
    //    }

    //    /// <summary>
    //    /// 转化整数为char
    //    /// </summary>
    //    private static char toHex(int n)
    //    {
    //        if (0 <= n && n <= 9) return (char)('0' + n);
    //        else if (10 <= n && n < 10 + 26) return (char)('a' + n - 10);
    //        else return ' ';
    //    }


    //    /// <summary>
    //    /// 获取method串的return至结尾
    //    /// </summary>
    //    public static String getLastReturn(String methodContent)
    //    {
    //        String str = "";
    //        int index = methodContent.LastIndexOf("return");
    //        if (index != -1) str = methodContent.Substring(index);

    //        return str;
    //    }

    //    /// <summary>
    //    /// 获取method串return前的部分
    //    /// </summary>
    //    public static String getBeforeReturn(String methodContent)
    //    {
    //        String str = "";

    //        int index = methodContent.LastIndexOf("return");
    //        if (index != -1) str = methodContent.Substring(0, index);

    //        return str;
    //    }

    //    /// <summary>
    //    /// 在method的逻辑开始处，插入语句
    //    /// </summary>
    //    public static String insertOnLogicBegin(String methodContent, String content)
    //    {
    //        int index = getMethodLogicIndex(methodContent);         // 获取return索引位置
    //        String Head = methodContent.Substring(0, index);        // method逻辑开始前的部分
    //        String Tail = methodContent.Substring(index);           // method逻辑开始后的部分

    //        String newContent = Head + content + "\r\n" + Tail; // 添加语句后的新的method
    //        return newContent;
    //    }


    //    /// <summary>
    //    /// 在return前插入语句
    //    /// </summary>
    //    public static String insertBeforeReturn(String methodContent, String content)
    //    {
    //        int index = methodContent.LastIndexOf("return");    // return索引位置
    //        String Head = methodContent.Substring(0, index);    // return前的部分
    //        String Tail = methodContent.Substring(index);       // return至结尾部分

    //        String newContent = Head + content + "\r\n    " + Tail; // 添加语句后的新的method
    //        return newContent;
    //    }
    //}

    ///// <summary>
    ///// 修改smali文件中的广告id信息
    ///// </summary>
    //class ModifySmaliAdId
    //{
    //    /** 加密或解密字符串，change加密、-change解密 */
    //    public static String Encryption(String str, int change)
    //    {
    //        if (str.Equals("") || str == null) return ""; // 空串不加密

    //        short sign = 1;
    //        if (change < 0)
    //        {
    //            sign = -1;
    //            change *= -1;
    //        }
    //        int num = 0;
    //        int tmp;

    //        char[] bytes = str.ToCharArray();
    //        for (int i = 0; i < bytes.Length; i++)
    //        {
    //            if (num == 0) num = change;

    //            // 限定在[0,127]之间
    //            tmp = bytes[i] + sign * (num % 3);
    //            if (tmp > 127) tmp -= 127;
    //            if (tmp < 0) tmp += 127;

    //            bytes[i] = (char)tmp;
    //            num /= 3;
    //        }
    //        str = new String(bytes);
    //        return new String(bytes);
    //    }

    //    /// <summary>
    //    /// 载入配置文件中的广告id映射信息
    //    /// </summary>
    //    public static Dictionary<String, String> getReplaceMap()
    //    {
    //        String ConfigPath1 = DependentFiles.toolsDir() + "AdUnVisibleIds.txt";
    //        String ConfigPath2 = DependentFiles.toolsDir() + "AdVisibleIds.txt";

    //        Dictionary<String, String> from = getConfigMap(ConfigPath1);
    //        Dictionary<String, String> to = getConfigMap(ConfigPath2);

    //        Dictionary<String, String> dic = getTransMap(from, to);
    //        return dic;
    //    }

    //    /// <summary>
    //    /// 将from中的id信息替换为
    //    /// AdmobBannerId:		ca-app-pub-2007808143875655/3037851725
    //    /// </summary>
    //    public static Dictionary<String, String> getTransMap(Dictionary<String, String> from, Dictionary<String, String> to)
    //    {
    //        Dictionary<String, String> dic = new Dictionary<String, String>();
    //        foreach (String key in from.Keys)
    //        {
    //            String fromValue = from[key];
    //            if (to.ContainsKey(key))
    //            {
    //                String toValue = to[key];

    //                if (!dic.ContainsKey(fromValue)) dic.Add(fromValue, toValue);
    //                else dic[fromValue] = toValue;
    //            }
    //        }

    //        return dic;
    //    }

    //    /// <summary>
    //    /// 载入文件中类似示例的键值对
    //    /// AdmobBannerId:		ca-app-pub-2007808143875655/3037851725
    //    /// </summary>
    //    public static Dictionary<String, String> getConfigMap(String ConfigPath)
    //    {
    //        Dictionary<String, String> dic = new Dictionary<String, String>();

    //        //String ConfigPath = DependentFiles.toolsDir() + "AdIdConfig.txt";
    //        String data = ReplaceValues.fileToString(ConfigPath);
    //        String[] configs = data.Replace("\r\n", "\n").Split('\n');
    //        foreach (String config in configs)
    //        {
    //            if (config.Contains(":"))
    //            {
    //                int index = config.IndexOf(":");
    //                String key = config.Substring(0, index).Trim();
    //                String value = config.Substring(index + 1).Trim();

    //                if (!dic.ContainsKey(key)) dic.Add(key, value);
    //                else dic[key] = value;
    //            }
    //        }

    //        return dic;
    //    }

    //    /// <summary>
    //    /// 替换指定的smali文件中的广告id信息
    //    /// </summary>
    //    public static void RepalceAdIds(String smali, Apk2Resource.Cmd.Callback call)
    //    {
    //        if (call != null) call(" ");
    //        if (call != null) call("【I】处理文件" + smali);
    //        if (call != null) call("【I】修改配置的广告id信息...");

    //        String data = ReplaceValues.fileToString(smali);    // 获取文件内容
    //        Dictionary<String, String> map = getReplaceMap();   // 载入配置的id信息

    //        bool modifyed = false;
    //        foreach (String key0 in map.Keys)
    //        {
    //            String key = "\"" + key0 + "\"";
    //            String value0 = map[key0];
    //            String value = "\"" + Encryption(value0, 65337) + "\"";     // 加密后的广告id串

    //            if (data.Contains(key))
    //            {
    //                data = data.Replace(key, value);
    //                if (call != null) call("【I】修改" + key0 + " -> " + value0);
    //                modifyed = true;
    //            }
    //        }

    //        if (modifyed)
    //        {
    //            ReplaceValues.SaveProcess(data, smali, true);
    //            if (call != null) call("【I】文件修改已保存");
    //        }
    //        if (call != null) call(" ");
    //    }
    //}

    ///// <summary>
    ///// 修改执行smali的指定方法中的参数值
    ///// </summary>
    //class ModifyLogic_resetAdIds
    //{
    //    /// <summary>
    //    /// 修改apk解包smali文件，在其中附加逻辑，输出广告id信息到文件
    //    /// 
    //    /// 添加文件 assets/perpre.dat			可由工具OneUtil4Perpre_cmd.jar生成
    //    /// 添加文件 lib/armeabi-v7a/libperpre.so
    //    /// 替换文件 smali\com\use\perpre \OneUtil4Modis.smali
    //    /// 替换文件 smali\com\joym\PaymentSdkV2\model \PaymentCUApplication.smali
    //    /// </summary>
    //    public static void ModfyId(String unpackPath, Apk2Resource.Cmd.Callback call)
    //    {
    //        if (call != null) call("【I】---");
    //        if (call != null) call("【I】广告id替换逻辑，修改开始...");
    //        String file = "";

    //        file = @"\smali\com\ltad\AdIds.smali";
    //        if (call != null) call("【I】添加文件" + file);
    //        DependentFiles.SaveFile(Resources.AdIds, unpackPath + file, true);

    //        file = @"\smali\com\ltad\LocalDB.smali";
    //        if (call != null) call("【I】添加文件" + file);
    //        DependentFiles.SaveFile(Resources.LocalDB, unpackPath + file, true);

    //        ModifySmaliAdId.RepalceAdIds(unpackPath + @"\smali\com\ltad\AdIds.smali", call);   // 修改文件中的广告id信息

    //        //在以下接口中调用函数，com.ltad.AdIds.Log_i(String tag, String msg)输出广告id信息

    //        //banner:
    //        //Ads_BannerId_Admob:	com.google.android.gms.ads.AdView.setAdUnitId(String adUnitId)
    //        //Ads_BannerId_Facebook:	com.facebook.ads.AdView.AdView(Context arg0, String arg1, AdSize arg2)	->arg1

    //        //fullScreen:
    //        //Ads_FullScreenId_Admob:		com.google.android.gms.ads.InterstitialAd.setAdUnitId(String adUnitId)
    //        //Ads_FullScreenId_Chartboost:	com.chartboost.sdk.Chartboost.startWithAppId(Activity activity, String appId, String appSignature)	->appId
    //        //Ads_FullScreenId_Facebook:	com.facebook.ads.InterstitialAd.InterstitialAd(Context arg0, String arg1)	-> arg1
    //        //Ads_FullScreenId_Unity:		com.unity3d.ads.android.UnityAds.init(Activity arg0, String arg1, IUnityAdsListener arg2)	->arg1

    //        // 获取文件配置信息
    //        String ConfigPath = DependentFiles.toolsDir() + "AdIdConfig.txt";
    //        String data = ReplaceValues.fileToString(ConfigPath);
    //        String[] configs = data.Replace("\r\n", "\n").Split('\n');
    //        foreach (String config in configs)
    //        {
    //            ModfyId(unpackPath, config, call);   // 执行配置修改逻辑
    //        }
    //        //if (call != null) call("【I】---");
    //        //if (call != null) call("【I】自打包修改结束！\r\n");
    //    }

    //    // Ads_BannerId_Admob:		com.google.android.gms.ads.AdView.setAdUnitId(1)
    //    // Ads_BannerId_Admob;com.google.android.gms.ads.AdView;setAdUnitId;1;
    //    public static void ModfyId(String unPackPath, String param0, Apk2Resource.Cmd.Callback call = null)
    //    {
    //        if (param0.Trim().Equals("")) return;
    //        String param = ModifyLogic_Log.paramFormat(param0);         // 格式化参数串

    //        // Ads_BannerId_Admob;com.google.android.gms.ads.AdView;setAdUnitId;0;
    //        // String AdIds_Key, String smaliPath, String method, String paramN
    //        String[] A = param.Split(';');
    //        if (A.Length == 4) ModfyId(unPackPath, A[1].Trim(), A[2].Trim(), A[3].Trim(), A[0].Trim(), call);
    //        else if (call != null) call("【W】参数格式有误，" + param0 + "\r\n示例：" + "Ads_BannerId_Admob: com.google.android.gms.ads.AdView.setAdUnitId(n)  n标识输出的为第几个参数");
    //    }

    //    /// <summary>
    //    /// 向smaliPath文件的method方法中注入信息输出逻辑，输出第N个位置处的param，输出AdIds中的Key值log信息
    //    /// </summary>
    //    /// <param name="smaliPath">com.google.android.gms.ads.AdView对应的smali文件</param>
    //    /// <param name="method">方法名称，如：setAdUnitId</param>
    //    /// <param name="paramN">p0或p1或p2</param>
    //    /// <param name="AdIds_Key">AdIds.smali中预先定义的固定值如：Ads_BannerId_Admob</param>
    //    public static void ModfyId(String unPackPath, String smaliPath, String method, String paramN, String AdIds_Key, Apk2Resource.Cmd.Callback call = null)
    //    {
    //        //com.facebook.ads.AdView.AdView
    //        if (smaliPath.EndsWith("." + method) || smaliPath.Equals(method)) method = "<init>";    // 构造函数默认名称
    //        String smali = unPackPath + "\\smali" + "\\" + smaliPath.Replace('.', '\\') + ".smali"; // 待修改的smali文件路径

    //        call(" ");
    //        call("【I】" + AdIds_Key + "：");

    //        // 获取文件内容
    //        String content = ReplaceValues.fileToString(smali);
    //        if (content.Equals(""))
    //        {
    //            if (call != null) call("【W】文件不存在，" + smali);
    //            return;
    //        }
    //        if (call != null)
    //        {
    //            call("【I】处理文件，" + smali);
    //        }

    //        // 获取method内容
    //        String methodContent = ModifySmali.getMethod(content, method);
    //        if (methodContent.Equals(""))
    //        {
    //            if (call != null) call("【W】文件中的method方法，" + method + "()不存在");
    //            return;
    //        }
    //        if (call != null) call("【I】修改method方法，" + method + "()");

    //        String newMethodContent = addModifyIdLogicToMethod(methodContent, paramN, AdIds_Key, call);
    //        if (!newMethodContent.Equals(""))
    //        {
    //            String newContent = content.Replace(methodContent, newMethodContent);
    //            ReplaceValues.SaveProcess(newContent, smali, true);
    //            if (call != null) call("【I】文件修改已保存");
    //        }
    //    }

    //    //if (resetAdId) adUnitId = AdmobBannerId;
    //    //    sget-boolean v0, Lcom/ltad/AdIds;->resetAdId:Z
    //    //    if-eqz v0, :cond_0
    //    //    sget-object p0, Lcom/ltad/AdIds;->AdmobBannerId:Ljava/lang/String;
    //    //    :cond_0

    //    /// <summary>
    //    /// 向method方法中添加广告id修改逻辑
    //    /// </summary>
    //    private static String addModifyIdLogicToMethod(String methodContent, String paramN0, String AdIds_Key, Apk2Resource.Cmd.Callback call = null)
    //    {
    //        String newMethodContent = "";

    //        if (!methodContent.Equals(""))
    //        {
    //            int paramN = Int32.Parse(paramN0);
    //            if (!ModifySmali.isStatic(methodContent)) paramN++;     // 非静态方法，多一个this的p0变量

    //            int localsN = ModifySmali.getLocals(methodContent);     // 内部变量数量
    //            String v0 = "v" + localsN;
    //            methodContent = methodContent.Replace(".locals " + localsN, ".locals " + (localsN + 1));   // 添加一个内部变量

    //            int condN = ModifySmali.getCond(methodContent);         // 获取内部cond最大值
    //            String cond_0 = ":cond_" + ModifySmali.ToHex(condN + 1);

    //            String key1 = "sget-boolean " + v0 + ", Lcom/ltad/AdIds;->resetAdId:Z";
    //            String key2 = "if-eqz " + v0 + ", " + cond_0;
    //            String key3 = "sget-object p" + paramN + ", Lcom/ltad/AdIds;->" + AdIds_Key + ":Ljava/lang/String;";
    //            String key4 = cond_0;

    //            if (!methodContent.Contains("->" + AdIds_Key + ":") || !methodContent.Contains("Lcom/ltad/AdIds;->resetAdId:Z"))
    //            {
    //                String appendStr = "\r\n    " + key1 + "\r\n    " + key2 + "\r\n    " + key3 + "\r\n    " + key4 + "\r\n    ";
    //                newMethodContent = ModifySmali.insertOnLogicBegin(methodContent, appendStr);    // 在方法逻辑开始出插入广告id修改逻辑

    //                if (call != null)
    //                {
    //                    call("【I】添加广告id赋值逻辑： if (resetAdId) p" + paramN + " = " + AdIds_Key + ";");     // if (resetAdId) adUnitId = AdmobBannerId;
    //                    call("【I】添加语句：" + "\r\n    " + appendStr.Trim());
    //                }
    //            }
    //            else if (call != null) call("【W】广告id赋值逻辑： if (resetAdId) p" + paramN + " = " + AdIds_Key + ";" + "已存在！");
    //        }

    //        return newMethodContent;
    //    }
    //}

    ///// <summary>
    ///// 向指定的smali文件指定方法中添加log输出逻辑
    ///// </summary>
    //class ModifyLogic_Log
    //{
    //    /// <summary>
    //    /// 修改apk解包smali文件，在其中附加逻辑，输出广告id信息到文件
    //    /// 
    //    /// 添加文件 assets/perpre.dat			可由工具OneUtil4Perpre_cmd.jar生成
    //    /// 添加文件 lib/armeabi-v7a/libperpre.so
    //    /// 替换文件 smali\com\use\perpre \OneUtil4Modis.smali
    //    /// 替换文件 smali\com\joym\PaymentSdkV2\model \PaymentCUApplication.smali
    //    /// </summary>
    //    public static void AddLog(String unpackPath, Apk2Resource.Cmd.Callback call)
    //    {
    //        if (call != null) call("【I】---");
    //        if (call != null) call("【I】附加广告id输出逻辑，修改开始...");
    //        String file = "";

    //        confimWritePermission(unpackPath, call);    // 确保写文件权限存在

    //        file = @"\smali\com\ltad\AdIds.smali";
    //        if (call != null) call("【I】添加文件" + file);
    //        DependentFiles.SaveFile(Resources.AdIds, unpackPath + file, true);

    //        file = @"\smali\com\ltad\LocalDB.smali";
    //        if (call != null) call("【I】添加文件" + file);
    //        DependentFiles.SaveFile(Resources.LocalDB, unpackPath + file, true);

    //        ModifySmaliAdId.RepalceAdIds(unpackPath + @"\smali\com\ltad\AdIds.smali", call);   // 修改文件中的广告id信息

    //        //在以下接口中调用函数，com.ltad.AdIds.Log_i(String tag, String msg)输出广告id信息

    //        //banner:
    //        //Ads_BannerId_Admob:	com.google.android.gms.ads.AdView.setAdUnitId(String adUnitId)
    //        //Ads_BannerId_Facebook:	com.facebook.ads.AdView.AdView(Context arg0, String arg1, AdSize arg2)	->arg1

    //        //fullScreen:
    //        //Ads_FullScreenId_Admob:		com.google.android.gms.ads.InterstitialAd.setAdUnitId(String adUnitId)
    //        //Ads_FullScreenId_Chartboost:	com.chartboost.sdk.Chartboost.startWithAppId(Activity activity, String appId, String appSignature)	->appId
    //        //Ads_FullScreenId_Facebook:	com.facebook.ads.InterstitialAd.InterstitialAd(Context arg0, String arg1)	-> arg1
    //        //Ads_FullScreenId_Unity:		com.unity3d.ads.android.UnityAds.init(Activity arg0, String arg1, IUnityAdsListener arg2)	->arg1

    //        // 获取文件配置信息
    //        String ConfigPath = DependentFiles.toolsDir() + "LogConfig.txt";
    //        String data = ReplaceValues.fileToString(ConfigPath);
    //        String[] configs = data.Replace("\r\n", "\n").Split('\n');
    //        foreach(String config in configs)
    //        {
    //            addLog(unpackPath, config, call);   // 执行配置修改逻辑
    //        }
    //        //if (call != null) call("【I】---");
    //        //if (call != null) call("【I】自打包修改结束！\r\n");
    //    }

    //    /// <summary>
    //    /// 格式化参数串
    //    /// Ads_BannerId_Admob:		com.google.android.gms.ads.AdView.setAdUnitId(1) -> 
    //    /// Ads_BannerId_Admob;com.google.android.gms.ads.AdView;setAdUnitId;1;
    //    /// </summary>
    //    public static String paramFormat(String param)
    //    {
    //        // 数据格式修改
    //        // Ads_BannerId_Admob:		com.google.android.gms.ads.AdView.setAdUnitId(0)
    //        if (param.Contains("(") && param.Contains("."))
    //        {
    //            int index = param.LastIndexOf(".");
    //            param = param.Substring(0, index) + ";" + param.Substring(index + 1);   // 替换最后一个“.”为“;”
    //        }
    //        if (param.Contains(")")) param = param.Replace(")", "");
    //        if (param.Contains(":")) param = param.Replace(":", ";");
    //        if (param.Contains("(")) param = param.Replace("(", ";");

    //        return param;
    //    }

    //    // Ads_BannerId_Admob:		com.google.android.gms.ads.AdView.setAdUnitId(1)
    //    // Ads_BannerId_Admob;com.google.android.gms.ads.AdView;setAdUnitId;1;
    //    public static void addLog(String unPackPath, String param0, Apk2Resource.Cmd.Callback call = null)
    //    {
    //        if (param0.Trim().Equals("")) return;
    //        String param = paramFormat(param0);         // 格式化参数串

    //        // Ads_BannerId_Admob;com.google.android.gms.ads.AdView;setAdUnitId;0;
    //        // String AdIds_Key, String smaliPath, String method, String paramN
    //        String[] A = param.Split(';');
    //        if(A.Length == 4) addLog(unPackPath, A[1].Trim(), A[2].Trim(), A[3].Trim(), A[0].Trim(), call);
    //        else if (call != null) call("【W】参数格式有误，" + param0 + "\r\n示例：" + "Ads_BannerId_Admob: com.google.android.gms.ads.AdView.setAdUnitId(n)  n标识输出的为第几个参数");
    //    }

    //    /// <summary>
    //    /// 向smaliPath文件的method方法中注入信息输出逻辑，输出第N个位置处的param，输出AdIds中的Key值log信息
    //    /// </summary>
    //    /// <param name="smaliPath">com.google.android.gms.ads.AdView对应的smali文件</param>
    //    /// <param name="method">方法名称，如：setAdUnitId</param>
    //    /// <param name="paramN">p0或p1或p2</param>
    //    /// <param name="AdIds_Key">AdIds.smali中预先定义的固定值如：Ads_BannerId_Admob</param>
    //    public static void addLog(String unPackPath, String smaliPath, String method, String paramN, String AdIds_Key, Apk2Resource.Cmd.Callback call = null)
    //    {
    //        //com.facebook.ads.AdView.AdView
    //        if (smaliPath.EndsWith("." + method) || smaliPath.Equals(method)) method = "<init>";    // 构造函数默认名称
    //        String smali = unPackPath + "\\smali" + "\\" + smaliPath.Replace('.', '\\') + ".smali"; // 待修改的smali文件路径

    //        call(" ");
    //        call("【I】" + AdIds_Key + "：");

    //        // 获取文件内容
    //        String content = ReplaceValues.fileToString(smali);
    //        if (content.Equals(""))
    //        {
    //            if (call != null) call("【W】文件不存在，" + smali);
    //            return;
    //        }
    //        if (call != null)
    //        {
    //            call("【I】处理文件，" + smali);
    //        }

    //        // 获取method内容
    //        String methodContent = ModifySmali.getMethod(content, method);
    //        if (methodContent.Equals(""))
    //        {
    //            if (call != null) call("【W】文件中的method方法，" + method + "()不存在");
    //            return;
    //        }
    //        if (call != null) call("【I】修改method方法，" + method + "()");

    //        String newMethodContent = addLogLogicToMethod(methodContent, paramN, AdIds_Key, call);
    //        if (!newMethodContent.Equals(""))
    //        {
    //            String newContent = content.Replace(methodContent, newMethodContent);
    //            ReplaceValues.SaveProcess(newContent, smali, true);
    //            if (call != null) call("【I】文件修改已保存");
    //        }
    //    }

    //    /// <summary>
    //    /// 向method方法中添加log输出调用逻辑
    //    /// </summary>
    //    private static String addLogLogicToMethod(String methodContent, String paramN0, String AdIds_Key, Apk2Resource.Cmd.Callback call = null)
    //    {
    //        String newMethodContent = "";

    //        if (!methodContent.Equals(""))
    //        {
    //            int paramN = Int32.Parse(paramN0);
    //            if (!ModifySmali.isStatic(methodContent)) paramN++;     // 非静态方法，多一个this的p0变量

    //            int localsN = ModifySmali.getLocals(methodContent);    // 内部变量数量
    //            String v0 = "v" + localsN;
    //            methodContent = methodContent.Replace(".locals " + localsN, ".locals " + (localsN + 1));   // 添加一个内部变量

    //            String key1 = "sget-object " + v0 + ", Lcom/ltad/AdIds;->" + AdIds_Key + ":Ljava/lang/String;";
    //            String key2 = "invoke-static {" + v0 + ", p" + paramN + "}, Lcom/ltad/AdIds;->Log_i(Ljava/lang/String;Ljava/lang/String;)V";

    //            if (!methodContent.Contains("->" + AdIds_Key + ":") || !methodContent.Contains("Lcom/ltad/AdIds;->Log_i("))
    //            {
    //                String appendStr = key1 + "\r\n    " + key2 + "\r\n    ";
    //                newMethodContent = ModifySmali.insertBeforeReturn(methodContent, appendStr);            // 在return前插入log输出逻辑

    //                if (call != null)
    //                {
    //                    call("【I】添加log输出项： Log_i(" + AdIds_Key + ", p" + paramN + ")"); //  Log_i(Ads_BannerId_Admob, adUnitId);
    //                    call("【I】添加语句：" + "\r\n    "+ appendStr.Trim());
    //                }
    //            }
    //            else if (call != null) call("【W】log输出项： Log_i(" + AdIds_Key + ", p" + paramN + ")" + "已存在！");
    //        }

    //        return newMethodContent;
    //    }

    //    /// <summary>
    //    /// 检测manifest.xml文件是否具有写权限，若无则添加
    //    /// </summary>
    //    /// <param name="unpackPath"></param>
    //    public static void confimWritePermission(String unpackPath, Apk2Resource.Cmd.Callback call = null)
    //    {
    //        String Manifest = unpackPath + "\\AndroidManifest.xml";
    //        String content = ReplaceValues.fileToString(Manifest);

    //        // 添加WRITE权限
    //        String writePermission = "<uses-permission android:name=\"android.permission.WRITE_EXTERNAL_STORAGE\"/>";
    //        if (!content.Equals("") && !content.Contains(writePermission))
    //        {
    //            if (call != null) call("【I】添加权限，AndroidManifest.xml（WRITE_EXTERNAL_STORAGE）");

    //            int index = content.LastIndexOf("</manifest>");
    //            content = content.Substring(0, index) + "\r\n    " + writePermission + "\r\n" + "</manifest>";

    //            ReplaceValues.SaveProcess(content, Manifest, true);
    //        }
    //        else if (call != null) call("【W】权限已存在，AndroidManifest.xml（WRITE_EXTERNAL_STORAGE）");
    //    }
    //}

}
