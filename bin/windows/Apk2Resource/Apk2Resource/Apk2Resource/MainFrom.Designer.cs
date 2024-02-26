namespace Apk2Resource
{
    partial class MainFrom
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainFrom));
            this.label1 = new System.Windows.Forms.Label();
            this.comboBox_sign = new System.Windows.Forms.ComboBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.Modify = new System.Windows.Forms.Button();
            this.dirDest = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 21);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 36;
            this.label1.Text = "游戏包：";
            // 
            // comboBox_sign
            // 
            this.comboBox_sign.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.comboBox_sign.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBox_sign.FormattingEnabled = true;
            this.comboBox_sign.Location = new System.Drawing.Point(377, 18);
            this.comboBox_sign.Name = "comboBox_sign";
            this.comboBox_sign.Size = new System.Drawing.Size(73, 20);
            this.comboBox_sign.TabIndex = 35;
            this.comboBox_sign.Visible = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.richTextBox1.Location = new System.Drawing.Point(13, 45);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(551, 327);
            this.richTextBox1.TabIndex = 34;
            this.richTextBox1.Text = "";
            // 
            // Modify
            // 
            this.Modify.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.Modify.Location = new System.Drawing.Point(456, 15);
            this.Modify.Name = "Modify";
            this.Modify.Size = new System.Drawing.Size(108, 26);
            this.Modify.TabIndex = 33;
            this.Modify.Text = "生成Resource";
            this.Modify.UseVisualStyleBackColor = true;
            this.Modify.Click += new System.EventHandler(this.Modify_Click);
            // 
            // dirDest
            // 
            this.dirDest.AllowDrop = true;
            this.dirDest.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dirDest.Location = new System.Drawing.Point(71, 18);
            this.dirDest.Name = "dirDest";
            this.dirDest.Size = new System.Drawing.Size(379, 21);
            this.dirDest.TabIndex = 32;
            this.dirDest.DragDrop += new System.Windows.Forms.DragEventHandler(this.dirDest_DragDrop);
            this.dirDest.DragEnter += new System.Windows.Forms.DragEventHandler(this.dirDest_DragEnter);
            // 
            // MainFrom
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(576, 388);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.comboBox_sign);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.Modify);
            this.Controls.Add(this.dirDest);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "MainFrom";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Apk -> Resource （打包资源生成工具）";
            this.Load += new System.EventHandler(this.MainFrom_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox comboBox_sign;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button Modify;
        private System.Windows.Forms.TextBox dirDest;
    }
}