using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Apk2Resource
{
    public partial class MainFrom : Form
    {
        public MainFrom()
        {
            InitializeComponent();
            dirDest.Text = ApkProcessLogic.toolTipInfo;
        }

        private void MainFrom_Load(object sender, EventArgs e)
        {
            ApkProcessLogic.loadSigns(comboBox_sign);      // 载入签名文件信息
        }

        private void dirDest_DragEnter(object sender, DragEventArgs e)
        {
            ApkProcessLogic.Form_DragEnter(sender, e);
        }

        private void dirDest_DragDrop(object sender, DragEventArgs e)
        {
            ApkProcessLogic.Form_DragDrop(sender, e);
        }


        private void Modify_Click(object sender, EventArgs e)
        {
            // 执行apk修改逻辑
            ApkProcessLogic.Modify_Click(this, Modify, richTextBox1, dirDest.Text, comboBox_sign.Text, Modify_Logic);
        }

        public static void Apk2ResourceLogic(String sourceApks)
        {
            // 执行apk修改逻辑
            ApkProcessLogic.Modify_Click(null, null, null, sourceApks, "", Modify_Logic);
        }

        private static void OutPut(String info)
        {
            ApkProcessLogic.OutPut(info);
        }

        /// <summary>
        /// 执行修改逻辑
        /// </summary>
        private static void Modify_Logic()
        {
            //OutPut("附加广告id信息log输出逻辑...");

            if (ApkProcessLogic.unpackPath.Equals("")) return;
            ModifyUnpakDir.Modify(ApkProcessLogic.unpackPath);


            //G:\sc\桌面快捷存储\其他\20190218\source配置_169_v1.2_jiuyao\combine\169_v1.2_jiuyao

            //// 添加广告id输出逻辑
            //if (checkBox_AddLog.Checked) ModifyLogic_Log.AddLog(path, OutPut);

            //// 修改广告id信息
            //if (checkBox_modifyAdId.Checked) ModifyLogic_resetAdIds.ModfyId(path, OutPut);
        }
    }
}
