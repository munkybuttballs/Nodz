from Qt import QtWidgets, QtCore

class NodzStandardWidget(QtWidgets.QWidget):
	"""docstring for NodzStandardWidget"""
	def __init__(self):

		super().__init__()

	def focusInEvent(self, event):
		print("focus!")
		super().focusInEvent(event)


class NodzLineEdit(QtWidgets.QLineEdit):

	classList = [str]
	focusIn   = QtCore.Signal(object)
	focusOut  = QtCore.Signal(object)
	def __init__(self, scene):

		super().__init__()
		self._scene = scene

	def scene(self):
		
		return self._scene

	def focusInEvent(self, event):

		self.focusIn.emit(self)
		super().focusInEvent(event)
		self.scene().subWidgetFocused = True

	def focusOutEvent(self, event):

		self.focusOut.emit(self)
		super().focusOutEvent(event)
		self.scene().subWidgetFocused = False

	def _connectUpdateObjectAttribute(self, function):
		
		self.textChanged.connect(function)

	def _setValue(self, value):
		
		return self.setText(value)

class NodzSpinBox(QtWidgets.QSpinBox):
	
	classList = [int]	
	focusIn   = QtCore.Signal(object)
	focusOut  = QtCore.Signal(object)
	def __init__(self, scene):

		super().__init__()
		self._scene = scene

	def scene(self):
		
		return self._scene

	def focusInEvent(self, event):

		self.focusIn.emit(self)
		super().focusInEvent(event)
		self.scene().subWidgetFocused = True

	def focusOutEvent(self, event):

		self.focusOut.emit(self)
		super().focusOutEvent(event)
		self.scene().subWidgetFocused = False

	def _connectUpdateObjectAttribute(self, function):
		
		self.valueChanged.connect(function)

	def _setValue(self, value):
		
		return self.setValue(value)


if __name__ == '__main__':
	print(NodzSpinBox.classList)