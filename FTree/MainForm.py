﻿import System.Drawing
import System.Windows.Forms
import System.IO

from System.Drawing import *
from System.Windows.Forms import *
from System.IO import *

def log(s):
	System.Diagnostics.Debug.WriteLine(s)

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()

		r_node = System.Windows.Forms.TreeNode("Node0")
		r_node.Text = "C:/"
		r_node.Name = "C:/"
		self._treeView1.Nodes.Add(r_node)

		for s in Directory.GetDirectories("C:/"):
			d_node = System.Windows.Forms.TreeNode("Node0")
			d_node.Name = d_node.Text = s[s.rfind("\\")+1:]
			r_node.Nodes.Add(d_node)
			try:
				for ss in Directory.GetFiles(s):
					f_node = System.Windows.Forms.TreeNode("Node1")
					f_node.Name = f_node.Text = ss[ss.rfind("\\")+1:]
					d_node.Nodes.AddRange(System.Array[System.Windows.Forms.TreeNode]([f_node]))
			except:
				pass

	def InitializeComponent(self):
		self._statusStrip1 = System.Windows.Forms.StatusStrip()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._splitContainer1 = System.Windows.Forms.SplitContainer()
		self._treeView1 = System.Windows.Forms.TreeView()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._webBrowser1 = System.Windows.Forms.WebBrowser()
		self._splitContainer1.BeginInit()
		self._splitContainer1.Panel1.SuspendLayout()
		self._splitContainer1.Panel2.SuspendLayout()
		self._splitContainer1.SuspendLayout()
		self.SuspendLayout()
		# 
		# statusStrip1
		# 
		self._statusStrip1.Location = System.Drawing.Point(0, 348)
		self._statusStrip1.Name = "statusStrip1"
		self._statusStrip1.Size = System.Drawing.Size(693, 22)
		self._statusStrip1.TabIndex = 1
		self._statusStrip1.Text = "statusStrip1"
		# 
		# menuStrip1
		# 
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(693, 24)
		self._menuStrip1.TabIndex = 2
		self._menuStrip1.Text = "menuStrip1"
		# 
		# splitContainer1
		# 
		self._splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
		self._splitContainer1.Location = System.Drawing.Point(0, 24)
		self._splitContainer1.Name = "splitContainer1"
		# 
		# splitContainer1.Panel1
		# 
		self._splitContainer1.Panel1.Controls.Add(self._treeView1)
		# 
		# splitContainer1.Panel2
		# 
		self._splitContainer1.Panel2.Controls.Add(self._webBrowser1)
		self._splitContainer1.Panel2.Controls.Add(self._comboBox1)
		self._splitContainer1.Size = System.Drawing.Size(693, 324)
		self._splitContainer1.SplitterDistance = 231
		self._splitContainer1.TabIndex = 3
		# 
		# treeView1
		# 
		self._treeView1.Dock = System.Windows.Forms.DockStyle.Fill
		self._treeView1.Location = System.Drawing.Point(0, 0)
		self._treeView1.Name = "treeView1"
		self._treeView1.Size = System.Drawing.Size(231, 324)
		self._treeView1.TabIndex = 0
		self._treeView1.AfterSelect += self.TreeView1AfterSelect
		# 
		# comboBox1
		# 
		self._comboBox1.Dock = System.Windows.Forms.DockStyle.Top
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(0, 0)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(458, 20)
		self._comboBox1.TabIndex = 0
		self._comboBox1.TextChanged += self.ComboBox1TextChanged
		# 
		# webBrowser1
		# 
		self._webBrowser1.Dock = System.Windows.Forms.DockStyle.Fill
		self._webBrowser1.Location = System.Drawing.Point(0, 20)
		self._webBrowser1.MinimumSize = System.Drawing.Size(20, 20)
		self._webBrowser1.Name = "webBrowser1"
		self._webBrowser1.Size = System.Drawing.Size(458, 304)
		self._webBrowser1.TabIndex = 1
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(693, 370)
		self.Controls.Add(self._splitContainer1)
		self.Controls.Add(self._statusStrip1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "FTree"
		self._splitContainer1.Panel1.ResumeLayout(False)
		self._splitContainer1.Panel2.ResumeLayout(False)
		self._splitContainer1.EndInit()
		self._splitContainer1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()

	def ComboBox1TextChanged(self, sender, e):
		self._webBrowser1.Navigate( self._comboBox1.Text)

	def TreeView1AfterSelect(self, sender, e):
		s = e.Node.FullPath
		if(Directory.Exists(s)):
			try:
				self._webBrowser1.Navigate("file:" + s)
			except:
				pass