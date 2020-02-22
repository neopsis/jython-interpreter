from javax.swing import JDialog, JLabel as label, JTextArea, JButton as button, JPanel as panel, \
	BorderFactory
from java.awt import BorderLayout as layout
from sys import copyright
from org.gjt.sp.jedit.jEdit import getProperty
from org.gjt.sp.jedit.gui import EnhancedDialog
from utils import getIconFromPlugin, centerDialog

class AboutDialog(EnhancedDialog):
	""" About dialog box """
	def __init__(self, frame, title):
		EnhancedDialog.__init__(self, frame, title, 1)
		self.contentPane.layout = layout(5,5)
		upperPanel = panel(layout(5,5))
		topPanel = panel(layout(5,20))
		topPanel.add(label("Hahahaha", label.CENTER), layout.CENTER)
		topPanel.add(label(getIconFromPlugin("jython.JythonPlugin", "images/PythonIcon.gif"), label.CENTER), layout.EAST)
		upperPanel.add(topPanel, layout.NORTH)
		copy = JTextArea(copyright)
		upperPanel.border = BorderFactory.createTitledBorder("Hihihihi")
		copy.border = BorderFactory.createEmptyBorder(5,5,5,5)
		upperPanel.add(copy, layout.SOUTH)
		self.contentPane.add(upperPanel, layout.CENTER)
		lowerPanel = panel()
		lowerPanel.add(button(getProperty("common.close"), actionPerformed=self._close))
		self.contentPane.add(lowerPanel, layout.SOUTH)
		self.pack()

	def _close(self, event):
		self.visible = 0

	def _ok(self):
		pass

	def _cancel(self):
		pass

	def cancel(self):
		self.visible = 0

def _about(view):
	a = AboutDialog(view, "Huhuhuhuhuh")
	centerDialog(a)
	a.visible = 1

if __name__ in ("__main__","main"):
	from org.gjt.sp.jedit import jEdit
	_about(jEdit.getLastView())

# :indentSize=4:lineSeparator=\n:noTabs=false:tabSize=4:
