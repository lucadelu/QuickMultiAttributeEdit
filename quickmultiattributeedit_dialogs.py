# --------------------------------------------------------
#    quickmultiattributeedit_dialogs - Dialog classes for quickmultiattributeedit
#
#    begin                : 19 May 2011
#    copyright            : (c) 2011 by Marco Braida
#    email                : See marcobra.ubuntu@gmail.com
#
#   QuickMultiAttributeEdit is free software and is offered 
#   without guarantee or warranty. You can redistribute it 
#   and/or modify it under the terms of version 2 of the 
#   GNU General Public License (GPL v2) as published by the 
#   Free Software Foundation (www.gnu.org).
# --------------------------------------------------------

import os.path
import operator

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from quickmultiattributeedit_library import *

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/forms")


# --------------------------------------------------------
#    quickmultiattributeedit_update_selected - Update selected feature field
# --------------------------------------------------------

from quickmultiattributeedit_update_selected_form import *

class quickmultiattributeedit_update_selected_dialog(QDialog, Ui_quickmultiattributeedit_update_selected_form):
	def __init__(self, iface):
		QDialog.__init__(self)
		self.iface = iface
		self.setupUi(self)
		#QObject.connect(self.browse, SIGNAL("clicked()"), self.browse_outfile)
        	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)

		#layer = self.iface.activeLayer() # layer attivo
	        layer = self.iface.mapCanvas().currentLayer()

		if (layer):
	                provider = layer.dataProvider()
			#provider.rewind()
			#feat = QgsFeature()
        	        #nameLayer = layer.name()
        	        # print nameLayer
			fields = provider.fields()
			if layer.type() == QgsMapLayer.VectorLayer:
				self.QLEvalore.setText("")
				self.CBfields.clear()
				#for name in fields:
				#	self.CBfields.addItem(fields[name].name())
				for (f_index, f) in fields.iteritems():
				    self.CBfields.addItem(f.name(), QVariant(f_index) )

			        if not layer.isEditable():
					infoString = QString("<font color='red'>Please activate the edit mode on the current <b>" + layer.name() + "</b> layer</font>")
					self.label.setText(infoString)
					#QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
					self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
					self.QLEvalore.setEnabled(False)
					self.CBfields.setEnabled(False)
				
				else:
	  				nF = layer.selectedFeatureCount()
					if (nF > 0):		
						self.label.setText("<font color='green'>For <b>" + str(nF) +  "</b> selected elements in <b>" + layer.name() + "</b> set value of field</font>" )
						self.CBfields.setFocus(True)
					else:
						infoString = QString("<font color='red'> Please select some elements into current <b>" + layer.name() + "</b> layer</font>")
						self.label.setText(infoString)
						#QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
						#self.buttonBox.setEnabled(False)
						self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
						self.QLEvalore.setEnabled(False)
						self.CBfields.setEnabled(False)
		else:
			infoString = QString("<font color='red'> <b>No layer selected... Please select a layer...</b></font>")
			#QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
			self.label.setText(infoString)
			self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
			self.QLEvalore.setEnabled(False)
			self.CBfields.setEnabled(False)

	def run(self):

	 layer = self.iface.mapCanvas().currentLayer()
         if (layer == None):
		infoString = QString("<font color='red'> <b>No layer selected... Please select a layer...</b></font>")
		#QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
		self.label.setText(infoString)
	        return
         if not layer.isEditable():
		infoString = QString("<font color='red'>Please activate the edit mode on the current <b>" + layer.name() + "</b> layer</font>")
		#QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
		self.label.setText(infoString)
	        return

         value = str(self.QLEvalore.displayText())
         nPosField = self.CBfields.currentIndex()
	 #QMessageBox.information(self.iface.mainWindow(), "Update selected", str(nPosField) )
         f_index = self.CBfields.itemData( nPosField ).toInt()[0]
	 #QMessageBox.information(self.iface.mainWindow(), "Update selected", str(f_index) )
         if len(value) <= 0:
		infoString = QString("Warning <b> please input a value... </b>")
         	#QMessageBox.information(self.iface.mainWindow(), "Update selected", "Please input a value...")
		self.label.setText(infoString)
         	return
	 layer = self.iface.mapCanvas().currentLayer()
	 #layer = self.iface.activeLayer()
	 if(layer):		
	  nF = layer.selectedFeatureCount()
	  if (nF > 0):		
	   #layer.startEditing()
	   oFea = layer.selectedFeaturesIds()
	   b = QVariant(value) # value of field
	   if (nF > 1):
		#for index, field in layer.dataProvider().fields().iteritems():
		#   if str(field.name()).lower() == "campo2":
		#            nPosField = index
		#            nPosField = self.CBfields.currentIndex()
		#     	QMessageBox.information(self.iface.mainWindow(), "Update selected", str(nPosField) )
		#if nPosField <= 0:
		#   return
	    for i in oFea:
	     layer.changeAttributeValue(int(i),f_index,b) 
	   else:
	    layer.changeAttributeValue(int(oFea[0]),f_index,b) # only one feature selected
	   infoString = QString("<font color='green'> <b>You can save or abort changes at the end of sessions.<br>Press the Save icon to save or disable the edit mode of layer without save changes to abort...</b></font>")
           QMessageBox.information(self.iface.mainWindow(),"Message",infoString)
	   #layer.commitChanges()
	  else:
	    QMessageBox.critical(self.iface.mainWindow(),"Error", "Please select at least one feature from <b> " + layer.name() + "</b> current layer")
	 else:
	  QMessageBox.critical(self.iface.mainWindow(),"Error","Please select a layer")





