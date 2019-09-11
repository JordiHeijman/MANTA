from __future__ import print_function, division
import sys
import os
sys.path.append('C:\\myokit\\myokit')
import myokit
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from os import walk
import csv 

print("MANTA is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.")

model1 = 0
model2 = 0
data1b = 1
data2b = 1
data1 = 1
data2 = 1
data1_ref = 1
data2_ref = 1
settingValuesforAAD = 0
 
import Qt5file

class MyWindowClass(QtWidgets.QMainWindow, Qt5file.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.statusBar()
        
        AADsdirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AADs")
        (_, _, filenames) = walk(AADsdirectory).next()
        for fn in filenames:
            if fn.endswith('.txt'):
                self.cmbAAD.addItem(fn[:(len(fn)-4)])   
                self.cmbAAD_3.addItem(fn[:(len(fn)-4)]) 
        
        self.cmbAAD.currentIndexChanged.connect(self.showAADInfo)
        self.spinAADConcentration.valueChanged.connect(self.processAADConcentration)
        
        self.spinICaL.valueChanged.connect(self.updateSlide)
        self.spinIK1.valueChanged.connect(self.updateSlide)
        self.spinIKr.valueChanged.connect(self.updateSlide)
        self.spinIKs.valueChanged.connect(self.updateSlide)
        self.spinIKur.valueChanged.connect(self.updateSlide)
        self.spinINa.valueChanged.connect(self.updateSlide)
        self.spinINaL.valueChanged.connect(self.updateSlide)
        self.spinINaK.valueChanged.connect(self.updateSlide)
        self.spinINCX.valueChanged.connect(self.updateSlide)
        self.spinIto.valueChanged.connect(self.updateSlide)
        
        self.ic50_ical_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_ik1_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_ikr_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_iks_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_ikur_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_ina_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_inal_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_inak_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_incx_aad1.valueChanged.connect(self.ic50_updatespin)
        self.ic50_ito_aad1.valueChanged.connect(self.ic50_updatespin)
        self.hill_ical_aad1.valueChanged.connect(self.ic50_updatespin)   
        self.hill_ik1_aad1.valueChanged.connect(self.ic50_updatespin)  
        self.hill_ikr_aad1.valueChanged.connect(self.ic50_updatespin)   
        self.hill_iks_aad1.valueChanged.connect(self.ic50_updatespin)   
        self.hill_ikur_aad1.valueChanged.connect(self.ic50_updatespin)   
        self.hill_ina_aad1.valueChanged.connect(self.ic50_updatespin)   
        self.hill_inal_aad1.valueChanged.connect(self.ic50_updatespin)   
        self.hill_inak_aad1.valueChanged.connect(self.ic50_updatespin)  
        self.hill_incx_aad1.valueChanged.connect(self.ic50_updatespin)   
        self.hill_ito_aad1.valueChanged.connect(self.ic50_updatespin)  

        self.ic50_ical_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_ik1_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_ikr_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_iks_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_ikur_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_ina_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_inal_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_inak_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_incx_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.ic50_ito_aad2.valueChanged.connect(self.ic50_updatespin2)
        self.hill_ical_aad2.valueChanged.connect(self.ic50_updatespin2)   
        self.hill_ik1_aad2.valueChanged.connect(self.ic50_updatespin2)  
        self.hill_ikr_aad2.valueChanged.connect(self.ic50_updatespin2)   
        self.hill_iks_aad2.valueChanged.connect(self.ic50_updatespin2)   
        self.hill_ikur_aad2.valueChanged.connect(self.ic50_updatespin2)   
        self.hill_ina_aad2.valueChanged.connect(self.ic50_updatespin2)   
        self.hill_inal_aad2.valueChanged.connect(self.ic50_updatespin2)   
        self.hill_inak_aad2.valueChanged.connect(self.ic50_updatespin2)  
        self.hill_incx_aad2.valueChanged.connect(self.ic50_updatespin2)   
        self.hill_ito_aad2.valueChanged.connect(self.ic50_updatespin2)  
        
        self.cmbAAD_3.currentIndexChanged.connect(self.showAADInfo)
        self.spinAADConcentration_3.valueChanged.connect(self.processAADConcentration)
        
        self.spinICaL_2.valueChanged.connect(self.updateSlide2)
        self.spinIK1_2.valueChanged.connect(self.updateSlide2)
        self.spinIKr_2.valueChanged.connect(self.updateSlide2)
        self.spinIKs_2.valueChanged.connect(self.updateSlide2)
        self.spinIKur_2.valueChanged.connect(self.updateSlide2)
        self.spinINa_2.valueChanged.connect(self.updateSlide2)
        self.spinINaL_2.valueChanged.connect(self.updateSlide2)
        self.spinINaK_2.valueChanged.connect(self.updateSlide2)
        self.spinINCX_2.valueChanged.connect(self.updateSlide2)
        self.spinIto_2.valueChanged.connect(self.updateSlide2)
        
        self.slideICaL_2.valueChanged.connect(self.updateSpin2)
        self.slideIK1_2.valueChanged.connect(self.updateSpin2)
        self.slideIKr_2.valueChanged.connect(self.updateSpin2)
        self.slideIKs_2.valueChanged.connect(self.updateSpin2)
        self.slideIKur_2.valueChanged.connect(self.updateSpin2)
        self.slideINa_2.valueChanged.connect(self.updateSpin2)
        self.slideINaL_2.valueChanged.connect(self.updateSpin2)
        self.slideINaK_2.valueChanged.connect(self.updateSpin2)
        self.slideINCX_2.valueChanged.connect(self.updateSpin2)
        self.slideIto_2.valueChanged.connect(self.updateSpin2)
        
        self.cmdRun.clicked.connect(self.startSimulation)
        self.cmdReset.clicked.connect(self.resetSimulation)
        
        #self.s1s2_button.clicked.connect(self.s1s2protocol)        
        
        self.export_1.clicked.connect(self.savecsv1)     
        self.export_2.clicked.connect(self.savecsv2)
        
        self.resetaxes_button.clicked.connect(self.resetaxes)
        
        self.cmbModel1.currentIndexChanged.connect(self.populateOutputBox)
        self.cmbOutput1Top.currentIndexChanged.connect(self.updateOutput)        
        self.cmbOutput1Bottom.currentIndexChanged.connect(self.updateOutput)      
              
        self.cmbModel2.currentIndexChanged.connect(self.populateOutputBox)
        self.cmbOutput2Top.currentIndexChanged.connect(self.updateOutput)        
        self.cmbOutput2Bottom.currentIndexChanged.connect(self.updateOutput) 
        
        self.markov_1.stateChanged.connect(self.markov_activation)
        self.markov_2.stateChanged.connect(self.markov_activation)
        
        self.xaxis_mdl1_from.valueChanged.connect(self.xaxis_adjustment1)
        self.xaxis_mdl1_to.valueChanged.connect(self.xaxis_adjustment1)
        self.xaxis_mdl2_from.valueChanged.connect(self.xaxis_adjustment2)
        self.xaxis_mdl2_to.valueChanged.connect(self.xaxis_adjustment2)
        self.chkEqualYAxis.stateChanged.connect(self.yaxis_equalizer)
        
        self.ref_mdl1_top.stateChanged.connect(self.plotselection)
        self.aad1_mdl1_top.stateChanged.connect(self.plotselection)
        self.aad2_mdl1_top.stateChanged.connect(self.plotselection)
        self.ref_mdl1_bottom.stateChanged.connect(self.plotselection)
        self.aad1_mdl1_bottom.stateChanged.connect(self.plotselection)
        self.aad2_mdl1_bottom.stateChanged.connect(self.plotselection)        
        self.ref_mdl2_top.stateChanged.connect(self.plotselection)
        self.aad1_mdl2_top.stateChanged.connect(self.plotselection)
        self.aad2_mdl2_top.stateChanged.connect(self.plotselection)
        self.ref_mdl2_bottom.stateChanged.connect(self.plotselection)
        self.aad1_mdl2_bottom.stateChanged.connect(self.plotselection)
        self.aad2_mdl2_bottom.stateChanged.connect(self.plotselection)     
        
        mdldirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
        (_, _, filenames) = walk(mdldirectory).next()
        for fn in filenames:
            if fn.endswith('.mmt'):
                self.cmbModel1.addItem(fn[:(len(fn)-4)])
                self.cmbModel2.addItem(fn[:(len(fn)-4)])

    def markov_activation(self):
        global settingValuesforAAD
        
        if self.sender().objectName() == 'markov_1':
            AAD = self.cmbAAD.currentText() 
            conc = self.spinAADConcentration.value()
        else:
            AAD = self.cmbAAD_3.currentText()
            conc = self.spinAADConcentration_3.value()
            
        with open (os.path.dirname(os.path.abspath(__file__)) + '/AADs/' + AAD + '.txt') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if row[0] == "INa":
                    AADs_line6 = float(row[1])
                    hill_line6 = float(row[2])
        
        if self.sender().objectName() == 'markov_1':
            self.ic50_ina_aad1.setValue(AADs_line6)
            self.hill_ina_aad1.setValue(hill_line6)
            AADs_line6b = self.ic50_ina_aad1.value()
            hill_line6b = self.hill_ina_aad1.value()
        else:
            self.ic50_ina_aad2.setValue(AADs_line6)
            self.hill_ina_aad2.setValue(hill_line6)
            AADs_line6b = self.ic50_ina_aad1.value()
            hill_line6b = self.hill_ina_aad1.value()
            
        blockINa = 0
        if conc > 0:
            blockINa = conc**hill_line6b / (conc**hill_line6b + AADs_line6b**hill_line6b)
        
        targetobj = self.spinINa_2
        targetslide = self.slideINa_2   
        targetlabel = self.ina_block2
        ic50_ina = self.ic50_ina_aad2
        hill_ina = self.hill_ina_aad2
        if self.sender().objectName() == 'markov_1':
            targetobj = self.spinINa
            targetslide = self.slideINa
            targetlabel = self.ina_block1
            ic50_ina = self.ic50_ina_aad1
            hill_ina = self.hill_ina_aad1       
            
        if self.sender().isChecked() == True:
            targetobj.setValue(100*0)
            targetobj.setEnabled(False)
            targetslide.setEnabled(False)  
            targetlabel.show()
            targetlabel.setNum(np.floor(100*blockINa))
            ic50_ina.setEnabled(False)
            hill_ina.setEnabled(False)
        else:
            targetobj.setValue(100*blockINa)
            targetobj.setEnabled(True)
            targetslide.setEnabled(True) 
            targetlabel.hide()
            ic50_ina.setEnabled(True)
            hill_ina.setEnabled(True)
            
    def processAADConcentration(self):
        global settingValuesforAAD
        if self.sender().objectName() == 'spinAADConcentration':
            AAD = self.cmbAAD.currentText() 
            conc = self.spinAADConcentration.value()
        else:
            AAD = self.cmbAAD_3.currentText()
            conc = self.spinAADConcentration_3.value()

        with open (os.path.dirname(os.path.abspath(__file__)) + '/AADs/' + AAD + '.txt') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if row[0] == "ICaL":
                    AADs_line1 = float(row[1])
                    hill_line1 = float(row[2])
                if row[0] == "IK1":
                    AADs_line2 = float(row[1])
                    hill_line2 = float(row[2])
                if row[0] == "IKr":
                    AADs_line3 = float(row[1])
                    hill_line3 = float(row[2])
                if row[0] == "IKs":
                    AADs_line4 = float(row[1])
                    hill_line4 = float(row[2])
                if row[0] == "IKur":
                    AADs_line5 = float(row[1])
                    hill_line5 = float(row[2])
                if row[0] == "INa":
                    AADs_line6 = float(row[1])
                    hill_line6 = float(row[2])
                if row[0] == "INaL":
                    AADs_line7 = float(row[1])
                    hill_line7 = float(row[2])
                if row[0] == "INaK":
                    AADs_line8 = float(row[1])
                    hill_line8 = float(row[2])
                if row[0] == "INCX":
                    AADs_line9 = float(row[1])  
                    hill_line9 = float(row[2])
                if row[0] == "Ito":
                    AADs_line10 = float(row[1])
                    hill_line10 = float(row[2])

        if self.sender().objectName() == 'spinAADConcentration':
            self.ic50_ical_aad1.setValue(AADs_line1)
            self.ic50_ik1_aad1.setValue(AADs_line2)
            self.ic50_ikr_aad1.setValue(AADs_line3)
            self.ic50_iks_aad1.setValue(AADs_line4)
            self.ic50_ikur_aad1.setValue(AADs_line5)
            self.ic50_ina_aad1.setValue(AADs_line6)            
            self.ic50_inal_aad1.setValue(AADs_line7)
            self.ic50_inak_aad1.setValue(AADs_line8)
            self.ic50_incx_aad1.setValue(AADs_line9)
            self.ic50_ito_aad1.setValue(AADs_line10)
            self.hill_ical_aad1.setValue(hill_line1)
            self.hill_ik1_aad1.setValue(hill_line2)
            self.hill_ikr_aad1.setValue(hill_line3)
            self.hill_iks_aad1.setValue(hill_line4)
            self.hill_ikur_aad1.setValue(hill_line5)
            self.hill_ina_aad1.setValue(hill_line6)
            self.hill_inal_aad1.setValue(hill_line7)
            self.hill_inak_aad1.setValue(hill_line8)
            self.hill_incx_aad1.setValue(hill_line9)
            self.hill_ito_aad1.setValue(hill_line10)
            AADs_line1b = self.ic50_ical_aad1.value()
            AADs_line2b = self.ic50_ik1_aad1.value()
            AADs_line3b = self.ic50_ikr_aad1.value()
            AADs_line4b = self.ic50_iks_aad1.value()
            AADs_line5b = self.ic50_ikur_aad1.value()
            AADs_line6b = self.ic50_ina_aad1.value()
            AADs_line7b = self.ic50_inal_aad1.value()
            AADs_line8b = self.ic50_inak_aad1.value()
            AADs_line9b = self.ic50_incx_aad1.value()
            AADs_line10b = self.ic50_ito_aad1.value()
            hill_line1b = self.hill_ical_aad1.value()   
            hill_line2b = self.hill_ik1_aad1.value()   
            hill_line3b = self.hill_ikr_aad1.value()   
            hill_line4b = self.hill_iks_aad1.value()   
            hill_line5b = self.hill_ikur_aad1.value()   
            hill_line6b = self.hill_ina_aad1.value()   
            hill_line7b = self.hill_inal_aad1.value()   
            hill_line8b = self.hill_inak_aad1.value()   
            hill_line9b = self.hill_incx_aad1.value()   
            hill_line10b = self.hill_ito_aad1.value()            
        else:
            self.ic50_ical_aad2.setValue(AADs_line1)
            self.ic50_ik1_aad2.setValue(AADs_line2)
            self.ic50_ikr_aad2.setValue(AADs_line3)
            self.ic50_iks_aad2.setValue(AADs_line4)
            self.ic50_ikur_aad2.setValue(AADs_line5)
            self.ic50_ina_aad2.setValue(AADs_line6)            
            self.ic50_inal_aad2.setValue(AADs_line7)
            self.ic50_inak_aad2.setValue(AADs_line8)
            self.ic50_incx_aad2.setValue(AADs_line9)
            self.ic50_ito_aad2.setValue(AADs_line10)
            self.hill_ical_aad2.setValue(hill_line1)
            self.hill_ik1_aad2.setValue(hill_line2)
            self.hill_ikr_aad2.setValue(hill_line3)
            self.hill_iks_aad2.setValue(hill_line4)
            self.hill_ikur_aad2.setValue(hill_line5)
            self.hill_ina_aad2.setValue(hill_line6)
            self.hill_inal_aad2.setValue(hill_line7)
            self.hill_inak_aad2.setValue(hill_line8)
            self.hill_incx_aad2.setValue(hill_line9)
            self.hill_ito_aad2.setValue(hill_line10)
            AADs_line1b = self.ic50_ical_aad2.value()
            AADs_line2b = self.ic50_ik1_aad2.value()
            AADs_line3b = self.ic50_ikr_aad2.value()
            AADs_line4b = self.ic50_iks_aad2.value()
            AADs_line5b = self.ic50_ikur_aad2.value()
            AADs_line6b = self.ic50_ina_aad2.value()
            AADs_line7b = self.ic50_inal_aad2.value()
            AADs_line8b = self.ic50_inak_aad2.value()
            AADs_line9b = self.ic50_incx_aad2.value()
            AADs_line10b = self.ic50_ito_aad2.value()
            hill_line1b = self.hill_ical_aad2.value()   
            hill_line2b = self.hill_ik1_aad2.value()   
            hill_line3b = self.hill_ikr_aad2.value()   
            hill_line4b = self.hill_iks_aad2.value()   
            hill_line5b = self.hill_ikur_aad2.value()   
            hill_line6b = self.hill_ina_aad2.value()   
            hill_line7b = self.hill_inal_aad2.value()   
            hill_line8b = self.hill_inak_aad2.value()   
            hill_line9b = self.hill_incx_aad2.value()   
            hill_line10b = self.hill_ito_aad2.value()            
            
        blockICaL = 0
        blockIK1 = 0
        blockIKr = 0
        blockIKs = 0
        blockIKur = 0
        blockINa = 0
        blockINaL = 0
        blockINaK = 0
        blockINCX = 0
        blockIto = 0

        if conc > 0:
            blockICaL = conc**hill_line1b / (conc**hill_line1b + AADs_line1b**hill_line1b)
            blockIK1 = conc**hill_line2b / (conc**hill_line2b + AADs_line2b**hill_line2b)
            blockIKr = conc**hill_line3b / (conc**hill_line3b + AADs_line3b**hill_line3b)
            blockIKs = conc**hill_line4b / (conc**hill_line4b + AADs_line4b**hill_line4b)
            blockIKur = conc**hill_line5b / (conc**hill_line5b + AADs_line5b**hill_line5b)
            blockINa = conc**hill_line6b / (conc**hill_line6b + AADs_line6b**hill_line6b)
            blockINaL = conc**hill_line7b / (conc**hill_line7b + AADs_line7b**hill_line7b)
            blockINaK = conc**hill_line8b / (conc**hill_line8b + AADs_line8b**hill_line8b)
            blockINCX = conc**hill_line9b / (conc**hill_line9b + AADs_line9b**hill_line9b)
            blockIto = conc**hill_line10b / (conc**hill_line10b + AADs_line10b**hill_line10b)  

        if self.sender().objectName() == 'spinAADConcentration':
            if AAD == 'Flecainide' or AAD == 'Lidocaine' or AAD == 'Vernakalant':
                settingValuesforAAD = 1
                self.spinICaL.setValue(100*blockICaL)
                self.spinIK1.setValue(100*blockIK1)
                self.spinIKr.setValue(100*blockIKr)
                self.spinIKs.setValue(100*blockIKs)
                self.spinIKur.setValue(100*blockIKur)
                self.spinINa.setValue(100*0)
                self.spinINa.setEnabled(False)
                self.slideINa.setEnabled(False)  
                self.markov_1.setEnabled(True)  
                self.markov_1.setChecked(True) 
                self.ina_block1.show()                             
                self.spinINaL.setValue(100*blockINaL)
                self.spinINaK.setValue(100*blockINaK)
                self.spinINCX.setValue(100*blockINCX)
                self.spinIto.setValue(100*blockIto)
                settingValuesforAAD = 0     
                
            elif AAD != '=Custom=':
                settingValuesforAAD = 1
                self.spinICaL.setValue(100*blockICaL)
                self.spinIK1.setValue(100*blockIK1)
                self.spinIKr.setValue(100*blockIKr)
                self.spinIKs.setValue(100*blockIKs)
                self.spinIKur.setValue(100*blockIKur)
                self.spinINa.setValue(100*blockINa)
                self.spinINa.setEnabled(True)
                self.slideINa.setEnabled(True)    
                self.markov_1.setEnabled(False)   
                self.markov_1.setChecked(False)
                self.ina_block1.hide()
                self.spinINaL.setValue(100*blockINaL)
                self.spinINaK.setValue(100*blockINaK)
                self.spinINCX.setValue(100*blockINCX)
                self.spinIto.setValue(100*blockIto)
                settingValuesforAAD = 0
    
            elif AAD == '=Custom=':
                self.spinAADConcentration.setEnabled(False)
                self.spinAADConcentration.setValue(0.0)  
                self.spinINa.setEnabled(True)
                self.slideINa.setEnabled(True) 
                self.markov_1.setEnabled(True)  
                self.markov_1.setChecked(False)  
                self.ina_block1.hide()
                #self.spinICaL.setValue(0.0)
                #self.spinIK1.setValue(0.0)
                #self.spinIKr.setValue(0.0)
                #self.spinIKs.setValue(0.0)
                #self.spinIKur.setValue(0.0)
                #self.spinINa.setValue(0.0)
                #self.spinINaL.setValue(0.0)
                #self.spinINaK.setValue(0.0)
                #self.spinINCX.setValue(0.0)
                #self.spinIto.setValue(0.0)  
             
        else:
            if AAD == 'Flecainide' or AAD == 'Lidocaine' or AAD == 'Vernakalant':
                settingValuesforAAD = 1
                self.spinICaL_2.setValue(100*blockICaL)
                self.spinIK1_2.setValue(100*blockIK1)
                self.spinIKr_2.setValue(100*blockIKr)
                self.spinIKs_2.setValue(100*blockIKs)
                self.spinIKur_2.setValue(100*blockIKur)
                self.spinINa_2.setValue(100*0)
                self.spinINa_2.setEnabled(False)
                self.slideINa_2.setEnabled(False) 
                self.markov_2.setEnabled(True)
                self.markov_2.setChecked(True)
                self.ina_block2.show()                
                self.spinINaL_2.setValue(100*blockINaL)
                self.spinINaK_2.setValue(100*blockINaK)
                self.spinINCX_2.setValue(100*blockINCX)
                self.spinIto_2.setValue(100*blockIto)
                settingValuesforAAD = 0
                
            elif AAD != '=Custom=':
                settingValuesforAAD = 1
                self.spinICaL_2.setValue(100*blockICaL)
                self.spinIK1_2.setValue(100*blockIK1)
                self.spinIKr_2.setValue(100*blockIKr)
                self.spinIKs_2.setValue(100*blockIKs)
                self.spinIKur_2.setValue(100*blockIKur)
                self.spinINa_2.setValue(100*blockINa)
                self.spinINa_2.setEnabled(True)
                self.slideINa_2.setEnabled(True)   
                self.markov_2.setEnabled(False)
                self.markov_2.setChecked(False)
                self.ina_block2.hide()                
                self.spinINaL_2.setValue(100*blockINaL)
                self.spinINaK_2.setValue(100*blockINaK)
                self.spinINCX_2.setValue(100*blockINCX)
                self.spinIto_2.setValue(100*blockIto)
                settingValuesforAAD = 0      
    
            elif AAD == '=Custom=':
                self.spinAADConcentration_3.setEnabled(False)
                self.spinAADConcentration_3.setValue(0.0)  
                self.spinINa_2.setEnabled(True)
                self.slideINa_2.setEnabled(True)   
                self.markov_2.setEnabled(True)  
                self.markov_2.setChecked(False)
                self.ina_block2.hide()                
                #self.spinICaL_2.setValue(0.0)
                #self.spinIK1_2.setValue(0.0)
                #self.spinIKr_2.setValue(0.0)
                #self.spinIKs_2.setValue(0.0)
                #self.spinIKur_2.setValue(0.0)
                #self.spinINa_2.setValue(0.0)
                #self.spinINaL_2.setValue(0.0)
                #self.spinINaK_2.setValue(0.0)
                #self.spinINCX_2.setValue(0.0)
                #self.spinIto_2.setValue(0.0)            
    
    def ic50_updatespin(self):
        global settingValuesforAAD
        
        AAD = self.cmbAAD.currentText() 
        conc = self.spinAADConcentration.value()
        
        AADs_line1b = self.ic50_ical_aad1.value()
        AADs_line2b = self.ic50_ik1_aad1.value()
        AADs_line3b = self.ic50_ikr_aad1.value()
        AADs_line4b = self.ic50_iks_aad1.value()
        AADs_line5b = self.ic50_ikur_aad1.value()
        AADs_line6b = self.ic50_ina_aad1.value()
        AADs_line7b = self.ic50_inal_aad1.value()
        AADs_line8b = self.ic50_inak_aad1.value()
        AADs_line9b = self.ic50_incx_aad1.value()
        AADs_line10b = self.ic50_ito_aad1.value()
        hill_line1b = self.hill_ical_aad1.value()   
        hill_line2b = self.hill_ik1_aad1.value()   
        hill_line3b = self.hill_ikr_aad1.value()   
        hill_line4b = self.hill_iks_aad1.value()   
        hill_line5b = self.hill_ikur_aad1.value()   
        hill_line6b = self.hill_ina_aad1.value()   
        hill_line7b = self.hill_inal_aad1.value()   
        hill_line8b = self.hill_inak_aad1.value()   
        hill_line9b = self.hill_incx_aad1.value()   
        hill_line10b = self.hill_ito_aad1.value()    
        
        blockICaL = conc**hill_line1b / (conc**hill_line1b + AADs_line1b**hill_line1b)
        blockIK1 = conc**hill_line2b / (conc**hill_line2b + AADs_line2b**hill_line2b)
        blockIKr = conc**hill_line3b / (conc**hill_line3b + AADs_line3b**hill_line3b)
        blockIKs = conc**hill_line4b / (conc**hill_line4b + AADs_line4b**hill_line4b)
        blockIKur = conc**hill_line5b / (conc**hill_line5b + AADs_line5b**hill_line5b)
        blockINa = conc**hill_line6b / (conc**hill_line6b + AADs_line6b**hill_line6b)
        blockINaL = conc**hill_line7b / (conc**hill_line7b + AADs_line7b**hill_line7b)
        blockINaK = conc**hill_line8b / (conc**hill_line8b + AADs_line8b**hill_line8b)
        blockINCX = conc**hill_line9b / (conc**hill_line9b + AADs_line9b**hill_line9b)
        blockIto = conc**hill_line10b / (conc**hill_line10b + AADs_line10b**hill_line10b)          

        if AAD == 'Flecainide' or AAD == 'Lidocaine' or AAD == 'Vernakalant':
            settingValuesforAAD = 1
            self.spinICaL.setValue(100*blockICaL)
            self.spinIK1.setValue(100*blockIK1)
            self.spinIKr.setValue(100*blockIKr)
            self.spinIKs.setValue(100*blockIKs)
            self.spinIKur.setValue(100*blockIKur)
            if self.markov_1.isChecked() == False:
                self.spinINa.setValue(100*blockINa)   
                #self.markov_1.setEnabled(True)                   
            self.spinINaL.setValue(100*blockINaL)
            self.spinINaK.setValue(100*blockINaK)
            self.spinINCX.setValue(100*blockINCX)
            self.spinIto.setValue(100*blockIto)
            settingValuesforAAD = 0   
        
        elif AAD != '=Custom=':
            settingValuesforAAD = 1
            self.spinICaL.setValue(100*blockICaL)
            self.spinIK1.setValue(100*blockIK1)
            self.spinIKr.setValue(100*blockIKr)
            self.spinIKs.setValue(100*blockIKs)
            self.spinIKur.setValue(100*blockIKur)
            self.spinINa.setValue(100*blockINa)
            self.spinINa.setEnabled(True)
            self.slideINa.setEnabled(True)    
            self.markov_1.setEnabled(False)   
            self.markov_1.setChecked(False)
            self.ina_block1.hide()
            self.spinINaL.setValue(100*blockINaL)
            self.spinINaK.setValue(100*blockINaK)
            self.spinINCX.setValue(100*blockINCX)
            self.spinIto.setValue(100*blockIto)
            settingValuesforAAD = 0

        elif AAD == '=Custom=':
            self.spinAADConcentration.setEnabled(False)
            self.spinAADConcentration.setValue(0.0)  
            self.spinINa.setEnabled(True)
            self.slideINa.setEnabled(True) 
            self.markov_1.setEnabled(True)  
            self.markov_1.setChecked(False)  
            self.ina_block1.hide()
            #self.spinICaL.setValue(0.0)
            #self.spinIK1.setValue(0.0)
            #self.spinIKr.setValue(0.0)
            #self.spinIKs.setValue(0.0)
            #self.spinIKur.setValue(0.0)
            #self.spinINa.setValue(0.0)
            #self.spinINaL.setValue(0.0)
            #self.spinINaK.setValue(0.0)
            #self.spinINCX.setValue(0.0)
            #self.spinIto.setValue(0.0)  

    def ic50_updatespin2(self):
        global settingValuesforAAD

        AAD = self.cmbAAD_3.currentText()
        conc = self.spinAADConcentration_3.value()

        AADs_line1b = self.ic50_ical_aad2.value()
        AADs_line2b = self.ic50_ik1_aad2.value()
        AADs_line3b = self.ic50_ikr_aad2.value()
        AADs_line4b = self.ic50_iks_aad2.value()
        AADs_line5b = self.ic50_ikur_aad2.value()
        AADs_line6b = self.ic50_ina_aad2.value()
        AADs_line7b = self.ic50_inal_aad2.value()
        AADs_line8b = self.ic50_inak_aad2.value()
        AADs_line9b = self.ic50_incx_aad2.value()
        AADs_line10b = self.ic50_ito_aad2.value()
        hill_line1b = self.hill_ical_aad2.value()   
        hill_line2b = self.hill_ik1_aad2.value()   
        hill_line3b = self.hill_ikr_aad2.value()   
        hill_line4b = self.hill_iks_aad2.value()   
        hill_line5b = self.hill_ikur_aad2.value()   
        hill_line6b = self.hill_ina_aad2.value()   
        hill_line7b = self.hill_inal_aad2.value()   
        hill_line8b = self.hill_inak_aad2.value()   
        hill_line9b = self.hill_incx_aad2.value()   
        hill_line10b = self.hill_ito_aad2.value()            
            
        blockICaL = conc**hill_line1b / (conc**hill_line1b + AADs_line1b**hill_line1b)
        blockIK1 = conc**hill_line2b / (conc**hill_line2b + AADs_line2b**hill_line2b)
        blockIKr = conc**hill_line3b / (conc**hill_line3b + AADs_line3b**hill_line3b)
        blockIKs = conc**hill_line4b / (conc**hill_line4b + AADs_line4b**hill_line4b)
        blockIKur = conc**hill_line5b / (conc**hill_line5b + AADs_line5b**hill_line5b)
        blockINa = conc**hill_line6b / (conc**hill_line6b + AADs_line6b**hill_line6b)
        blockINaL = conc**hill_line7b / (conc**hill_line7b + AADs_line7b**hill_line7b)
        blockINaK = conc**hill_line8b / (conc**hill_line8b + AADs_line8b**hill_line8b)
        blockINCX = conc**hill_line9b / (conc**hill_line9b + AADs_line9b**hill_line9b)
        blockIto = conc**hill_line10b / (conc**hill_line10b + AADs_line10b**hill_line10b)  

        if AAD == 'Flecainide' or AAD == 'Lidocaine' or AAD == 'Vernakalant':
            settingValuesforAAD = 1
            self.spinICaL_2.setValue(100*blockICaL)
            self.spinIK1_2.setValue(100*blockIK1)
            self.spinIKr_2.setValue(100*blockIKr)
            self.spinIKs_2.setValue(100*blockIKs)
            self.spinIKur_2.setValue(100*blockIKur)
            if self.markov_2.isChecked() == False:
                self.spinINa_2.setValue(100*blockINa)
                #self.markov_2.setEnabled(True) 
            self.spinINaL_2.setValue(100*blockINaL)
            self.spinINaK_2.setValue(100*blockINaK)
            self.spinINCX_2.setValue(100*blockINCX)
            self.spinIto_2.setValue(100*blockIto)
            settingValuesforAAD = 0 

        elif AAD != '=Custom=':
            settingValuesforAAD = 1
            self.spinICaL_2.setValue(100*blockICaL)
            self.spinIK1_2.setValue(100*blockIK1)
            self.spinIKr_2.setValue(100*blockIKr)
            self.spinIKs_2.setValue(100*blockIKs)
            self.spinIKur_2.setValue(100*blockIKur)
            self.spinINa_2.setValue(100*blockINa)
            self.spinINa_2.setEnabled(True)
            self.slideINa_2.setEnabled(True)   
            self.markov_2.setEnabled(False)
            self.markov_2.setChecked(False)
            self.ina_block2.hide()                
            self.spinINaL_2.setValue(100*blockINaL)
            self.spinINaK_2.setValue(100*blockINaK)
            self.spinINCX_2.setValue(100*blockINCX)
            self.spinIto_2.setValue(100*blockIto)
            settingValuesforAAD = 0      

        elif AAD == '=Custom=':
            self.spinAADConcentration_3.setEnabled(False)
            self.spinAADConcentration_3.setValue(0.0)  
            self.spinINa_2.setEnabled(True)
            self.slideINa_2.setEnabled(True)   
            self.markov_2.setEnabled(True)  
            self.markov_2.setChecked(False)
            self.ina_block2.hide()                
            #self.spinICaL_2.setValue(0.0)
            #self.spinIK1_2.setValue(0.0)
            #self.spinIKr_2.setValue(0.0)
            #self.spinIKs_2.setValue(0.0)
            #self.spinIKur_2.setValue(0.0)
            #self.spinINa_2.setValue(0.0)
            #self.spinINaL_2.setValue(0.0)
            #self.spinINaK_2.setValue(0.0)
            #self.spinINCX_2.setValue(0.0)
            #self.spinIto_2.setValue(0.0)                       
        
    def showAADInfo(self):
        global settingValuesforAAD        
        AAD = self.sender().currentText()
        #conc = self.spinAADConcentration.value()

        if self.sender().objectName() == 'cmbAAD':
            self.spinAADConcentration.setEnabled(True)
            self.spinAADConcentration.setValue(10.0)        
            self.spinAADConcentration.setValue(0.0)   
            self.ic50_aad1_lbl.setText(AAD)
    
            with open (os.path.dirname(os.path.abspath(__file__)) + '/AADs/' + AAD + '.txt') as f:
                reader = csv.reader(f, delimiter='\t')
                for row in reader:
                    if row[0] == "Antiarrhythmic drug class":
                        self.aadc1.setText(row[1])
                    if row[0] == "Effective range":
                        self.er1.setText(row[1])    
        else:
            self.spinAADConcentration_3.setEnabled(True)
            self.spinAADConcentration_3.setValue(10.0)              
            self.spinAADConcentration_3.setValue(0.0)        
            self.ic50_aad2_lbl.setText(AAD)            
            
            with open (os.path.dirname(os.path.abspath(__file__)) + '/AADs/' + AAD + '.txt') as f:
                reader = csv.reader(f, delimiter='\t')
                for row in reader:
                    if row[0] == "Antiarrhythmic drug class":
                        self.aadc2.setText(row[1])
                    if row[0] == "Effective range":
                        self.er2.setText(row[1])  
                

    def updateSlide(self):
        global settingValuesforAAD
        AAD = self.cmbAAD.currentText()
        sending_spin = self.sender()
        
        if sending_spin.objectName() == 'spinICaL':
            self.slideICaL.setValue(sending_spin.value())
        
        if sending_spin.objectName() == 'spinIK1':
            self.slideIK1.setValue(sending_spin.value())

        if sending_spin.objectName() == 'spinIKr':
            self.slideIKr.setValue(sending_spin.value())
        
        if sending_spin.objectName() == 'spinIKs':
            self.slideIKs.setValue(sending_spin.value())

        if sending_spin.objectName() == 'spinIKur':
            self.slideIKur.setValue(sending_spin.value())

        if sending_spin.objectName() == 'spinINa':
            self.slideINa.setValue(sending_spin.value())

        if sending_spin.objectName() == 'spinINaL':
            self.slideINaL.setValue(sending_spin.value())

        if sending_spin.objectName() == 'spinINaK':
            self.slideINaK.setValue(sending_spin.value())

        if sending_spin.objectName() == 'spinINCX':
            self.slideINCX.setValue(sending_spin.value())

        if sending_spin.objectName() == 'spinIto':
            self.slideIto.setValue(sending_spin.value())
        
        if settingValuesforAAD == 0:
            if AAD == "Flecainide" or AAD == "Lidocaine" or AAD == "Vernakalant":
                self.cmbAAD.currentText()
            else:
                self.cmbAAD.setCurrentIndex(0)

    def updateSlide2(self):
        global settingValuesforAAD
        AAD = self.cmbAAD_3.currentText()
        sending_spin2 = self.sender()
        
        if sending_spin2.objectName() == 'spinICaL_2':
            self.slideICaL_2.setValue(sending_spin2.value())
        
        if sending_spin2.objectName() == 'spinIK1_2':
            self.slideIK1_2.setValue(sending_spin2.value())

        if sending_spin2.objectName() == 'spinIKr_2':
            self.slideIKr_2.setValue(sending_spin2.value())
        
        if sending_spin2.objectName() == 'spinIKs_2':
            self.slideIKs_2.setValue(sending_spin2.value())

        if sending_spin2.objectName() == 'spinIKur_2':
            self.slideIKur_2.setValue(sending_spin2.value())

        if sending_spin2.objectName() == 'spinINa_2':
            self.slideINa_2.setValue(sending_spin2.value())

        if sending_spin2.objectName() == 'spinINaL_2':
            self.slideINaL_2.setValue(sending_spin2.value())

        if sending_spin2.objectName() == 'spinINaK_2':
            self.slideINaK_2.setValue(sending_spin2.value())

        if sending_spin2.objectName() == 'spinINCX_2':
            self.slideINCX_2.setValue(sending_spin2.value())

        if sending_spin2.objectName() == 'spinIto_2':
            self.slideIto_2.setValue(sending_spin2.value())
        
        if settingValuesforAAD == 0:
            if AAD == "Flecainide" or AAD == "Lidocaine" or AAD == "Vernakalant":
                self.cmbAAD_3.currentText()
            else:            
                self.cmbAAD_3.setCurrentIndex(0)

    def updateSpin2(self):
        global settingValuesforAAD
        sending_slide2 = self.sender()
        
        if sending_slide2.objectName() == 'slideICaL_2':
            self.spinICaL_2.setValue(sending_slide2.value())
        
        if sending_slide2.objectName() == 'slideIK1_2':
            self.spinIK1_2.setValue(sending_slide2.value())

        if sending_slide2.objectName() == 'slideIKr_2':
            self.spinIKr_2.setValue(sending_slide2.value())
        
        if sending_slide2.objectName() == 'slideIKs_2':
            self.spinIKs_2.setValue(sending_slide2.value())

        if sending_slide2.objectName() == 'slideIKur_2':
            self.spinIKur_2.setValue(sending_slide2.value())

        if sending_slide2.objectName() == 'slideINa_2':
            self.spinINa_2.setValue(sending_slide2.value())

        if sending_slide2.objectName() == 'slideINaL_2':
            self.spinINaL_2.setValue(sending_slide2.value())

        if sending_slide2.objectName() == 'slideINaK_2':
            self.spinINaK_2.setValue(sending_slide2.value())

        if sending_slide2.objectName() == 'slideINCX_2':
            self.spinINCX_2.setValue(sending_slide2.value())

        if sending_slide2.objectName() == 'slideIto_2':
            self.spinIto_2.setValue(sending_slide2.value())
            
    def populateOutputBox(self):
        global model1, model2
        global data1, data2
        global data1_ref, data2_ref
        
        sending_cmb = self.sender()
        mdldirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
        mdlname = sending_cmb.currentText() + ".mmt"
        mdlpath = mdldirectory + "\\" + mdlname
        print(mdlname)
                
        if sending_cmb.objectName() == 'cmbModel1': 
            data1 = 1
            model1, p1, s1 = myokit.load(mdlpath)

            self.cmbOutput1Top.clear()
            self.cmbOutput1Bottom.clear()
            #for s in model1.states():
            #    self.cmbOutput1Top.addItem(s.qname())
            #    self.cmbOutput1Bottom.addItem(s.qname())
            
            self.startSimulation(1)
            self.ref_mdl1_top.setChecked(True)
            self.aad1_mdl1_top.setChecked(True)
            self.aad2_mdl1_top.setChecked(True)
            self.ref_mdl1_bottom.setChecked(True)
            self.aad1_mdl1_bottom.setChecked(True)
            self.aad2_mdl1_bottom.setChecked(True)            
            self.ina_block1.hide()
            
            #print(data1.variable_info())
            model_vars = data1[0].variable_info()
            for items in sorted(model_vars):                
                self.cmbOutput1Top.addItem(items)
                self.cmbOutput1Bottom.addItem(items)
            
            ind_Vm_top = self.cmbOutput1Top.findText('output.Vm')
            if ind_Vm_top >= 0:
                self.cmbOutput1Top.setCurrentIndex(ind_Vm_top)
                
            ind_Cai_bottom = self.cmbOutput1Bottom.findText('output.Cai')
            if ind_Cai_bottom >= 0:
                self.cmbOutput1Bottom.setCurrentIndex(ind_Cai_bottom)
                
        else:
            data2 = 1
            model2, p1, s1 = myokit.load(mdlpath)
            
            self.cmbOutput2Top.clear()
            self.cmbOutput2Bottom.clear()
            
            self.startSimulation(2)
            self.ref_mdl2_top.setChecked(True)
            self.aad1_mdl2_top.setChecked(True)
            self.aad2_mdl2_top.setChecked(True)
            self.ref_mdl2_bottom.setChecked(True)
            self.aad1_mdl2_bottom.setChecked(True)
            self.aad2_mdl2_bottom.setChecked(True)    
            self.ina_block2.hide()
            
            model_vars = data2[0].variable_info()
            for items in sorted(model_vars):                
                self.cmbOutput2Top.addItem(items)
                self.cmbOutput2Bottom.addItem(items)
            
            ind_Vm_top = self.cmbOutput2Top.findText('output.Vm')
            if ind_Vm_top >= 0:
                self.cmbOutput2Top.setCurrentIndex(ind_Vm_top)
                
            ind_Cai_bottom = self.cmbOutput2Bottom.findText('output.Cai')
            if ind_Cai_bottom >= 0:
                self.cmbOutput2Bottom.setCurrentIndex(ind_Cai_bottom)

        
    def updateOutput(self):
        global data1b        
        global data2b
        global data1
        global data2
        global data1_ref
        global data2_ref
        global model1
        global model2
        
        sending_cmb = self.sender()
        print("Sender = " + sending_cmb.objectName())
        
        if sending_cmb.currentText() != "":
        
            if sending_cmb.objectName() == 'cmbOutput1Top':
                if data1 != 1:
                    self.mplOutput1Top.axes.clear()
                    self.mplOutput1Top.axes.hold(True)
                    for k, item in enumerate(data1):
                        cur_data1_ref = data1_ref[k]
                        cur_data1 = data1[k]
                        cur_data1b = data1b[k]
                        if self.aad1_mdl1_top.isChecked():                        
                            self.mplOutput1Top.axes.plot(cur_data1[model1.time()],cur_data1[sending_cmb.currentText()],'-r')
                        if self.aad2_mdl1_top.isChecked():                        
                            self.mplOutput1Top.axes.plot(cur_data1b[model1.time()],cur_data1b[sending_cmb.currentText()],'-b')
                        if self.ref_mdl1_top.isChecked():                        
                            self.mplOutput1Top.axes.plot(cur_data1_ref[model1.time()],cur_data1_ref[sending_cmb.currentText()],'-k')
                        self.mplOutput1Top.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())
                #else:
                #    self.mplOutput1Top.axes.plot(data1_ref[model1.time()],data1_ref[sending_cmb.currentText()],'-k')
                self.mplOutput1Top.draw()

            if sending_cmb.objectName() == 'cmbOutput1Bottom':
                if data1 != 1:
                    self.mplOutput1Bottom.axes.clear()
                    self.mplOutput1Bottom.axes.hold(True)
                    for k, item in enumerate(data1):
                        cur_data1_ref = data1_ref[k]
                        cur_data1 = data1[k]
                        cur_data1b = data1b[k]                        
                        if self.aad1_mdl1_bottom.isChecked():                        
                            self.mplOutput1Bottom.axes.plot(cur_data1[model1.time()],cur_data1[sending_cmb.currentText()],'-r')
                        if self.aad2_mdl1_bottom.isChecked():                        
                            self.mplOutput1Bottom.axes.plot(cur_data1b[model1.time()],cur_data1b[sending_cmb.currentText()],'-b')
                        if self.ref_mdl1_bottom.isChecked():                        
                            self.mplOutput1Bottom.axes.plot(cur_data1_ref[model1.time()],cur_data1_ref[sending_cmb.currentText()],'-k')
                        self.mplOutput1Bottom.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())            
                    #self.mplOutput1Bottom.axes.plot(data1[model1.time()],data1[sending_cmb.currentText()],'-r', data1b[model1.time()],data1b[sending_cmb.currentText()],'-b', data1_ref[model1.time()],data1_ref[sending_cmb.currentText()],'-k')
                #else:
                #    self.mplOutput1Bottom.axes.plot(data1_ref[model1.time()],data1_ref[sending_cmb.currentText()],'-k')
                self.mplOutput1Bottom.draw()
            
            if sending_cmb.objectName() == 'cmbOutput2Top':
                if data2 != 1:
                    self.mplOutput2Top.axes.clear()
                    self.mplOutput2Top.axes.hold(True)
                    for k, item in enumerate(data2):
                        cur_data2_ref = data2_ref[k]
                        cur_data2 = data2[k]
                        cur_data2b = data2b[k]    
                        if self.aad1_mdl2_top.isChecked():                        
                            self.mplOutput2Top.axes.plot(cur_data2[model2.time()],cur_data2[sending_cmb.currentText()],'-r')
                        if self.aad2_mdl2_top.isChecked():                        
                            self.mplOutput2Top.axes.plot(cur_data2b[model2.time()],cur_data2b[sending_cmb.currentText()],'-b')
                        if self.ref_mdl2_top.isChecked():                        
                            self.mplOutput2Top.axes.plot(cur_data2_ref[model2.time()],cur_data2_ref[sending_cmb.currentText()],'-k')
                        self.mplOutput2Top.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())
                    #self.mplOutput2Top.axes.plot(data2[model2.time()],data2[sending_cmb.currentText()],'-r', data2b[model2.time()],data2b[sending_cmb.currentText()],'-b', data2_ref[model2.time()],data2_ref[sending_cmb.currentText()],'-k')
                #else:
                    #self.mplOutput2Top.axes.plot(data2_ref[model2.time()],data2_ref[sending_cmb.currentText()],'-k')
                self.mplOutput2Top.draw()
            
            if sending_cmb.objectName() == 'cmbOutput2Bottom':
                if data2 != 1:
                    self.mplOutput2Bottom.axes.clear()
                    self.mplOutput2Bottom.axes.hold(True)
                    for k, item in enumerate(data2):
                        cur_data2_ref = data2_ref[k]
                        cur_data2 = data2[k]
                        cur_data2b = data2b[k] 
                        if self.aad1_mdl2_bottom.isChecked():                        
                            self.mplOutput2Bottom.axes.plot(cur_data2[model2.time()],cur_data2[sending_cmb.currentText()],'-r')
                        if self.aad2_mdl2_bottom.isChecked():                        
                            self.mplOutput2Bottom.axes.plot(cur_data2b[model2.time()],cur_data2b[sending_cmb.currentText()],'-b')
                        if self.ref_mdl2_bottom.isChecked():                        
                            self.mplOutput2Bottom.axes.plot(cur_data2_ref[model2.time()],cur_data2_ref[sending_cmb.currentText()],'-k')
                        self.mplOutput2Bottom.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())                
                    #self.mplOutput2Bottom.axes.plot(data2[model2.time()],data2[sending_cmb.currentText()],'-r', data2b[model2.time()],data2b[sending_cmb.currentText()],'-b', data2_ref[model2.time()],data2_ref[sending_cmb.currentText()],'-k')
                #else:
                    #self.mplOutput2Bottom.axes.plot(data2_ref[model2.time()],data2_ref[sending_cmb.currentText()],'-k')
                self.mplOutput2Bottom.draw()

    def resetSimulation(self):
        global settingValuesforAAD
        
        self.slideICaL.setSliderPosition(0)
        self.slideIK1.setSliderPosition(0)
        self.slideIKr.setSliderPosition(0)
        self.slideIKs.setSliderPosition(0)
        self.slideIKur.setSliderPosition(0)
        self.slideINa.setSliderPosition(0)
        self.slideINaL.setSliderPosition(0)
        self.slideINaK.setSliderPosition(0)
        self.slideINCX.setSliderPosition(0)
        self.slideIto.setSliderPosition(0)
        
        self.spinICaL.setValue(0)
        self.spinIK1.setValue(0)
        self.spinIKr.setValue(0)
        self.spinIKs.setValue(0)
        self.spinIKur.setValue(0)
        self.spinINa.setValue(0)
        self.spinINaL.setValue(0)
        self.spinINaK.setValue(0)
        self.spinINCX.setValue(0)
        self.spinIto.setValue(0)        
        
        self.slideICaL_2.setSliderPosition(0)
        self.slideIK1_2.setSliderPosition(0)
        self.slideIKr_2.setSliderPosition(0)
        self.slideIKs_2.setSliderPosition(0)
        self.slideIKur_2.setSliderPosition(0)
        self.slideINa_2.setSliderPosition(0)
        self.slideINaL_2.setSliderPosition(0)
        self.slideINaK_2.setSliderPosition(0)
        self.slideINCX_2.setSliderPosition(0)
        self.slideIto_2.setSliderPosition(0)

        self.spinICaL_2.setValue(0)
        self.spinIK1_2.setValue(0)
        self.spinIKr_2.setValue(0)
        self.spinIKs_2.setValue(0)
        self.spinIKur_2.setValue(0)
        self.spinINa_2.setValue(0)
        self.spinINaL_2.setValue(0)
        self.spinINaK_2.setValue(0)
        self.spinINCX_2.setValue(0)
        self.spinIto_2.setValue(0)   
        
        self.txtRateModel1.setText("60")
        self.spinStimDur1.setValue(1.0)
        self.spinStimAmp1.setValue(100)
        self.spinPrepacingModel1.setValue(10)
        self.spinShowbeatsModel1.setValue(3)
        self.txtS1S2IntervalsModel1.setText("100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,320,340,360,380,400,420,440,460,480,520,560")
        
        self.txtRateModel2.setText("60")
        self.spinStimDur2.setValue(1.0)
        self.spinStimAmp2.setValue(100)
        self.spinPrepacingModel2.setValue(10)
        self.spinShowbeatsModel2.setValue(3)
        self.txtS1S2IntervalsModel2.setText("100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,320,340,360,380,400,420,440,460,480,520,560")
        
        self.spinCao1.setValue(1.80)
        self.spinKo1.setValue(5.40)
        self.spinNao1.setValue(140.00)
        self.spinCao2.setValue(1.80)
        self.spinKo2.setValue(5.40)
        self.spinNao2.setValue(140.00)
        
        self.xaxis_mdl1_from.setValue(0)
        self.xaxis_mdl1_to.setValue(1000) 
        self.xaxis_mdl2_from.setValue(0)
        self.xaxis_mdl2_to.setValue(1000)
        self.chkEqualYAxis.setChecked(False)
        
        self.spinAADConcentration.setValue(0.0)    
        self.spinAADConcentration_3.setValue(0.0)  
        
        self.markov_1.setChecked(False)
        self.markov_2.setChecked(False)
        
        self.checks1s2_mdl1.setChecked(False)
        self.checks1s2_mdl2.setChecked(False)
        
        self.ref_mdl1_top.setChecked(True)
        self.aad1_mdl1_top.setChecked(True)
        self.aad2_mdl1_top.setChecked(True)
        self.ref_mdl1_bottom.setChecked(True)
        self.aad1_mdl1_bottom.setChecked(True)
        self.aad2_mdl1_bottom.setChecked(True)
        self.ref_mdl2_top.setChecked(True)
        self.aad1_mdl2_top.setChecked(True)
        self.aad2_mdl2_top.setChecked(True)
        self.ref_mdl2_bottom.setChecked(True)
        self.aad1_mdl2_bottom.setChecked(True)
        self.aad2_mdl2_bottom.setChecked(True)
        
        if settingValuesforAAD == 0:
            self.cmbAAD.setCurrentIndex(0)
            self.cmbAAD_3.setCurrentIndex(0)

        
    def startSimulation(self, flag=3):                  # CtoF button event handler
        global model1, data1, data1_ref, data1b
        global model2, data2, data2_ref, data2b
        #global protocol1, protocol2
        if flag == False:
            flag = 3
            
        print("Simulation starting... flag = " + str(flag))
        progrep = MyokitProgressReporter(self.statusBar())
        
        s1s2 = self.txtS1S2IntervalsModel1.text().split(",")
        
        if flag == 1 or flag == 3:
            #Extract BCLs
            bcls = self.txtRateModel1.text().split(",")
            data1_ref = []
            data1 = []
            data1b = []
            self.mplOutput1Top.axes.clear()
            self.mplOutput1Bottom.axes.clear()
            self.lblAPDCaTModel1Ctrl.setText("")
            self.lblAPDCaTModel1Alt.setText("")
            self.lblAPDCaTModel1Alt_2.setText("")
            for k, bcl_text in enumerate(bcls):             
                bcl = 1000 * 60.0 / float(bcl_text) #self.spinRateModel1.value()
                stimdur = self.spinStimDur1.value()
                stimamp = 0.01 * self.spinStimAmp1.value()
                prebeats = self.spinPrepacingModel1.value()
                showbeats = self.spinShowbeatsModel1.value()
                  
                p = myokit.Protocol()
                p.schedule(stimamp,10,stimdur,bcl,0)
                
                s = myokit.Simulation(model1, p)
                s.set_constant('parameters.Ca_o', self.spinCao1.value())
                s.set_constant('parameters.K_o', self.spinKo1.value())
                s.set_constant('parameters.Na_o', self.spinNao1.value())            
                progrep.msgvar = "Model 1 - Control Condition -"
                s.pre(prebeats*bcl, progress=progrep)
                data1_ref_temp = s.run(showbeats*bcl, progress=progrep, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                data1_ref.append(data1_ref_temp)                
                apds1_ref = data1_ref_temp.apd(v='output.Vm', threshold=0.9*np.min(data1_ref_temp['output.Vm']))
                CaT_ref = np.max(data1_ref_temp['output.Cai']) - np.min(data1_ref_temp['output.Cai']) 
                #Syst_ref = np.max(data1_ref_temp['output.Cai'])                       
                #Diast_ref = np.min(data1_ref_temp['output.Cai'])
                dvdt_ref = np.diff(data1_ref_temp['output.Vm']) / np.diff(data1_ref_temp[model1.time()])
                dvdtmax_ref = np.max(dvdt_ref)     
                if len(apds1_ref) > 0:
                    self.lblAPDCaTModel1Ctrl.setText("%s\n %.1f Hz REF - APD: %d ms // dV/dt_max: %d mV/ms // CaT: %d nM" % (self.lblAPDCaTModel1Ctrl.text(), (1000/bcl), apds1_ref['duration'][0], dvdtmax_ref, 1000*CaT_ref))
                else:
                    self.lblAPDCaTModel1Ctrl.setText("%s\n %.1f Hz REF - APD: ? ms // dV/dt_max: ? mV/ms // CaT: ? nM" % (self.lblAPDCaTModel1Ctrl.text()), (1000/bcl))  

                if self.checks1s2_mdl1.isChecked():
                    peakrefval = np.max(data1_ref_temp['output.Vm'])
                    ERP_ref = 0
                    state = s.state()
                    print("Running S1S2 protocol - REF:Model1")
                    #data= np.zeros(100)
                    for ks2, cur_s1s2 in enumerate(s1s2):
                        p2 = myokit.Protocol()
                        p2.schedule(stimamp,10,stimdur,bcl,0) 
                        p2.schedule(stimamp,10+float(cur_s1s2),stimdur,bcl,1)
                        s.set_protocol(p2)
                        s.reset() 
                        s.set_state(state)
                        d2 = s.run(bcl, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                        data1_ref.append(d2)
                        
                        d_trim = d2.trim_left(0.75 * apds1_ref['duration'][0])#apds1_s1s2[0][1])
                        peakval = np.max(d_trim['output.Vm'])
                        if peakval > 0.8*peakrefval and ERP_ref == 0:
                            ERP_ref = float(cur_s1s2)
                    
                    self.lblAPDCaTModel1Ctrl.setText("%s\n REF - ERP: %d ms" % (self.lblAPDCaTModel1Ctrl.text(), ERP_ref))
               #mdlname = "models/" + self.cmbModel1.currentText() + ".mmt"
                #print(mdlname)
               
                #m1, p1, s1 = myokit.load(mdlname)
                s = myokit.Simulation(model1, p)
                s.set_constant('parameters.Ca_o', self.spinCao1.value())
                s.set_constant('parameters.K_o', self.spinKo1.value())
                s.set_constant('parameters.Na_o', self.spinNao1.value())            
    
                s.set_constant('parameters.ICaL_Block', self.spinICaL.value() / 100.0)
                s.set_constant('parameters.IK1_Block', self.spinIK1.value() / 100.0)
                s.set_constant('parameters.IKr_Block', self.spinIKr.value() / 100.0)
                s.set_constant('parameters.IKs_Block', self.spinIKs.value() / 100.0)
                s.set_constant('parameters.IKur_Block', self.spinIKur.value() / 100.0)
                s.set_constant('parameters.INa_Block', self.spinINa.value() / 100.0)
                s.set_constant('parameters.INaL_Block', self.spinINaL.value() / 100.0)
                s.set_constant('parameters.INaK_Block', self.spinINaK.value() / 100.0)
                s.set_constant('parameters.INCX_Block', self.spinINCX.value() / 100.0)
                s.set_constant('parameters.Ito_Block', self.spinIto.value() / 100.0)
                s.set_constant('I_Na_Markov.new_drug_mode', 0)                
                
                if self.cmbAAD.currentText()=='Flecainide': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 3)
                elif self.cmbAAD.currentText()=='Lidocaine': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 2)
                elif self.cmbAAD.currentText()=='Vernakalant': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 4)
    
                if self.markov_1.isChecked() == True:
                    s.set_constant('I_Na_Markov.conc', self.spinAADConcentration.value() / 1e6)
                else:
                    s.set_constant('I_Na_Markov.conc', 0)
                    
                progrep.msgvar = "Model 1 - With Blocker -"
                s.pre(prebeats*bcl, progress=progrep)
                data1_temp = s.run(showbeats*bcl, progress=progrep, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                data1.append(data1_temp)               
                apds1_alt = data1_temp.apd(v='output.Vm', threshold=0.9*np.min(data1_temp['output.Vm']))
                CaT_alt = np.max(data1_temp['output.Cai']) - np.min(data1_temp['output.Cai']) 
                #Syst_alt = np.max(data1_temp['output.Cai'])                       
                #Diast_alt = np.min(data1_temp['output.Cai'])   
                dvdt_alt = np.diff(data1_temp['output.Vm']) / np.diff(data1_temp[model1.time()])
                dvdtmax_alt = np.max(dvdt_alt)                               
                #self.lblAPDCaTModel2Alt.setText('APD: ' + str(apds2_alt[0]) + ' ms / CaT: ' + str(CaT_alt) + ' uM')
                if len(apds1_alt) > 0:
                    self.lblAPDCaTModel1Alt.setText("%s\n %.1f Hz AAD1 - APD: %d ms // dV/dt_max: %d mV/ms // CaT: %d nM" % (self.lblAPDCaTModel1Alt.text(), (1000/bcl), apds1_alt['duration'][0], dvdtmax_alt, 1000*CaT_alt))
                else:
                    self.lblAPDCaTModel1Alt.setText("%s\n %.1f Hz AAD1 - APD: ? ms // dV/dt_max: ? mV/ms // CaT: ? nM" % (self.lblAPDCaTModel1Alt.text()), (1000/bcl))            
                
                if self.checks1s2_mdl1.isChecked():
                    peakrefval = np.max(data1_temp['output.Vm'])
                    ERP_ref = 0                    
                    state = s.state()
                    print("Running S1S2 protocol - AAD1:Model1")
                    for ks2, cur_s1s2 in enumerate(s1s2):
                        p2 = myokit.Protocol()
                        p2.schedule(stimamp,10,stimdur,bcl,0) 
                        p2.schedule(stimamp,10+float(cur_s1s2),stimdur,bcl,1)
                        s.set_protocol(p2)
                        s.reset() 
                        s.set_state(state)
                        d2 = s.run(bcl, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                        data1.append(d2)

                        d_trim = d2.trim_left(0.75 * apds1_alt['duration'][0])#apds1_s1s2[0][1])
                        peakval = np.max(d_trim['output.Vm'])
                        if peakval > 0.8*peakrefval and ERP_ref == 0:
                            ERP_ref = float(cur_s1s2)
                    
                    self.lblAPDCaTModel1Alt.setText("%s\n AAD1 - ERP: %d ms" % (self.lblAPDCaTModel1Alt.text(), ERP_ref))
                        
                s = myokit.Simulation(model1, p)
                s.set_constant('parameters.Ca_o', self.spinCao1.value())
                s.set_constant('parameters.K_o', self.spinKo1.value())
                s.set_constant('parameters.Na_o', self.spinNao1.value())            
    
                s.set_constant('parameters.ICaL_Block', self.spinICaL_2.value() / 100.0)
                s.set_constant('parameters.IK1_Block', self.spinIK1_2.value() / 100.0)
                s.set_constant('parameters.IKr_Block', self.spinIKr_2.value() / 100.0)
                s.set_constant('parameters.IKs_Block', self.spinIKs_2.value() / 100.0)
                s.set_constant('parameters.IKur_Block', self.spinIKur_2.value() / 100.0)
                s.set_constant('parameters.INa_Block', self.spinINa_2.value() / 100.0)
                s.set_constant('parameters.INaL_Block', self.spinINaL_2.value() / 100.0)
                s.set_constant('parameters.INaK_Block', self.spinINaK_2.value() / 100.0)
                s.set_constant('parameters.INCX_Block', self.spinINCX_2.value() / 100.0)
                s.set_constant('parameters.Ito_Block', self.spinIto_2.value() / 100.0)
                s.set_constant('I_Na_Markov.new_drug_mode', 0)                

                if self.cmbAAD_3.currentText()=='Flecainide': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 3)
                elif self.cmbAAD_3.currentText()=='Lidocaine': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 2)
                elif self.cmbAAD_3.currentText()=='Vernakalant': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 4)          
    
                if self.markov_2.isChecked() == True:
                    s.set_constant('I_Na_Markov.conc', self.spinAADConcentration_3.value() / 1e6)
                else:
                    s.set_constant('I_Na_Markov.conc', 0)
                
                progrep.msgvar = "Model 1 - With Another Blocker -"
                s.pre(prebeats*bcl, progress=progrep)
                data1b_temp = s.run(showbeats*bcl, progress=progrep, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                data1b.append(data1b_temp)                
                apds1b_alt = data1b_temp.apd(v='output.Vm', threshold=0.9*np.min(data1b_temp['output.Vm']))
                CaTb_alt = np.max(data1b_temp['output.Cai']) - np.min(data1b_temp['output.Cai']) 
                #Systb_alt = np.max(data1b_temp['output.Cai'])                       
                #Diastb_alt = np.min(data1b_temp['output.Cai'])                         
                dvdtb_alt = np.diff(data1b_temp['output.Vm']) / np.diff(data1b_temp[model1.time()])
                dvdtmaxb_alt = np.max(dvdtb_alt)                                   
                #self.lblAPDCaTModel2Alt.setText('APD: ' + str(apds2_alt[0]) + ' ms / CaT: ' + str(CaT_alt) + ' uM')
                if len(apds1b_alt) > 0:
                    self.lblAPDCaTModel1Alt_2.setText("%s\n %.1f Hz AAD2 - APD: %d ms // dV/dt_max: %d mV/ms // CaT: %d nM" % (self.lblAPDCaTModel1Alt_2.text(), (1000/bcl), apds1b_alt['duration'][0], dvdtmaxb_alt, 1000*CaTb_alt))
                else:
                    self.lblAPDCaTModel1Alt_2.setText("%s\n %.1f Hz AAD2 - APD: ? ms // dV/dt_max: ? mV/ms // CaT: ? nM" % (self.lblAPDCaTModel1Alt_2.text()), (1000/bcl))            
                
                if self.checks1s2_mdl1.isChecked():
                    peakrefval = np.max(data1b_temp['output.Vm'])
                    ERP_ref = 0                           
                    state = s.state()
                    print("Running S1S2 protocol - AAD2:Model1")
                    #data= np.zeros(100)
                    for ks2, cur_s1s2 in enumerate(s1s2):
                        p2 = myokit.Protocol()
                        p2.schedule(stimamp,10,stimdur,bcl,0) 
                        p2.schedule(stimamp,10+float(cur_s1s2),stimdur,bcl,1)
                        s.set_protocol(p2)
                        s.reset() 
                        s.set_state(state)
                        d2 = s.run(bcl, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                        data1b.append(d2)                

                        d_trim = d2.trim_left(0.75 * apds1b_alt['duration'][0])#apds1_s1s2[0][1])
                        peakval = np.max(d_trim['output.Vm'])
                        if peakval > 0.8*peakrefval and ERP_ref == 0:
                            ERP_ref = float(cur_s1s2)
                    
                    self.lblAPDCaTModel1Alt_2.setText("%s\n AAD2 - ERP: %d ms" % (self.lblAPDCaTModel1Alt_2.text(), ERP_ref))
               
            if len(self.cmbOutput1Top.currentText()) > 1:
                self.mplOutput1Top.axes.hold(True)
                self.mplOutput1Bottom.axes.hold(True)
                for k, item in enumerate(data1):
                    data1_temp = data1[k]
                    data1b_temp = data1b[k]
                    data1_ref_temp = data1_ref[k] 
                    if self.aad1_mdl1_top.isChecked():
                        self.mplOutput1Top.axes.plot(data1_temp[model1.time()],data1_temp[self.cmbOutput1Top.currentText()],'-r')
                    if self.aad2_mdl1_top.isChecked():
                        self.mplOutput1Top.axes.plot(data1b_temp[model1.time()],data1b_temp[self.cmbOutput1Top.currentText()],'-b')
                    if self.ref_mdl1_top.isChecked():
                        self.mplOutput1Top.axes.plot(data1_ref_temp[model1.time()],data1_ref_temp[self.cmbOutput1Top.currentText()],'-k')
                    if self.aad1_mdl1_bottom.isChecked():
                        self.mplOutput1Bottom.axes.plot(data1_temp[model1.time()],data1_temp[self.cmbOutput1Bottom.currentText()],'-r')
                    if self.aad2_mdl1_bottom.isChecked():
                        self.mplOutput1Bottom.axes.plot(data1b_temp[model1.time()],data1b_temp[self.cmbOutput1Bottom.currentText()],'-b')
                    if self.ref_mdl1_bottom.isChecked():
                        self.mplOutput1Bottom.axes.plot(data1_ref_temp[model1.time()],data1_ref_temp[self.cmbOutput1Bottom.currentText()],'-k')
                self.mplOutput1Top.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())
                self.mplOutput1Bottom.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())
                self.mplOutput1Top.draw()                
                self.mplOutput1Bottom.draw()
                        
##########End of for bcls model 1
        s1s2_2 = self.txtS1S2IntervalsModel2.text().split(",")
        
        if flag == 2 or flag == 3:
            bcls = self.txtRateModel2.text().split(",")
            data2_ref = []
            data2 = []
            data2b = []
            self.mplOutput2Top.axes.clear()
            self.mplOutput2Bottom.axes.clear()
            self.lblAPDCaTModel2Ctrl.setText("")
            self.lblAPDCaTModel2Alt.setText("")
            self.lblAPDCaTModel2Alt_2.setText("")
            for k, bcl_text in enumerate(bcls):            
                bcl = 1000 * 60.0 / float(bcl_text)
                stimdur = self.spinStimDur2.value()
                stimamp = 0.01 * self.spinStimAmp2.value()
                prebeats = self.spinPrepacingModel2.value()
                showbeats = self.spinShowbeatsModel2.value()
                  
                p = myokit.Protocol()
                p.schedule(stimamp,10,stimdur,bcl,0)
                
                s = myokit.Simulation(model2, p)
                s.set_constant('parameters.Ca_o', self.spinCao2.value())
                s.set_constant('parameters.K_o', self.spinKo2.value())
                s.set_constant('parameters.Na_o', self.spinNao2.value())      
                progrep.msgvar = "Model 2 - Control Condition -"
                s.pre(prebeats*bcl, progress=progrep)                        
                data2_ref_temp = s.run(showbeats*bcl, progress=progrep, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                data2_ref.append(data2_ref_temp)
                apds2_ref = data2_ref_temp.apd(v='output.Vm', threshold=0.9*np.min(data2_ref_temp['output.Vm']))
                CaT2_ref = np.max(data2_ref_temp['output.Cai']) - np.min(data2_ref_temp['output.Cai'])
                #Syst2_ref = np.max(data2_ref_temp['output.Cai'])
                #Diast2_ref = np.min(data2_ref_temp['output.Cai'])            
                dvdt2_ref = np.diff(data2_ref_temp['output.Vm']) / np.diff(data2_ref_temp[model2.time()])
                dvdtmax2_ref = np.max(dvdt2_ref) 
                if len(apds2_ref) > 0:
                    self.lblAPDCaTModel2Ctrl.setText("%s\n %.1f Hz REF - APD: %d ms // dV/dt_max: %d mV/ms // CaT: %d nM" % (self.lblAPDCaTModel2Ctrl.text(), (1000/bcl), apds2_ref['duration'][0], dvdtmax2_ref, 1000*CaT2_ref))
                else:
                    self.lblAPDCaTModel2Ctrl.setText("%s\n %.1f Hz REF - APD: ? ms // dV/dt_max: ? mV/ms // CaT: ? nM" % (self.lblAPDCaTModel2Ctrl.text()), (1000/bcl))  

                if self.checks1s2_mdl2.isChecked():
                    peakrefval = np.max(data2_ref_temp['output.Vm'])
                    ERP_ref = 0
                    state = s.state()
                    print("Running S1S2 protocol - REF:Model2")
                    for ks2, cur_s1s2 in enumerate(s1s2_2):
                        p2 = myokit.Protocol()
                        p2.schedule(stimamp,10,stimdur,bcl,0) 
                        p2.schedule(stimamp,10+float(cur_s1s2),stimdur,bcl,1)
                        s.set_protocol(p2)
                        s.reset() 
                        s.set_state(state)
                        d2 = s.run(bcl, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                        data2_ref.append(d2)
                        
                        d_trim = d2.trim_left(0.75 * apds2_ref['duration'][0])#apds1_s1s2[0][1])
                        peakval = np.max(d_trim['output.Vm'])
                        if peakval > 0.8*peakrefval and ERP_ref == 0:
                            ERP_ref = float(cur_s1s2)
                    
                    self.lblAPDCaTModel2Ctrl.setText("%s\n REF - ERP: %d ms" % (self.lblAPDCaTModel2Ctrl.text(), ERP_ref))

                s = myokit.Simulation(model2, p)
                s.set_constant('parameters.Ca_o', self.spinCao2.value())
                s.set_constant('parameters.K_o', self.spinKo2.value())
                s.set_constant('parameters.Na_o', self.spinNao2.value())  
                
                s.set_constant('parameters.ICaL_Block', self.spinICaL.value() / 100.0)
                s.set_constant('parameters.IK1_Block', self.spinIK1.value() / 100.0)
                s.set_constant('parameters.IKr_Block', self.spinIKr.value() / 100.0)
                s.set_constant('parameters.IKs_Block', self.spinIKs.value() / 100.0)
                s.set_constant('parameters.IKur_Block', self.spinIKur.value() / 100.0)
                s.set_constant('parameters.INa_Block', self.spinINa.value() / 100.0)
                s.set_constant('parameters.INaL_Block', self.spinINaL.value() / 100.0)
                s.set_constant('parameters.INaK_Block', self.spinINaK.value() / 100.0)
                s.set_constant('parameters.INCX_Block', self.spinINCX.value() / 100.0)
                s.set_constant('parameters.Ito_Block', self.spinIto.value() / 100.0)
                s.set_constant('I_Na_Markov.new_drug_mode', 0)
                
                if self.cmbAAD.currentText()=='Flecainide': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 3)
                elif self.cmbAAD.currentText()=='Lidocaine': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 2)
                elif self.cmbAAD.currentText()=='Vernakalant': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 4)
                
                if self.markov_1.isChecked() == True:
                    s.set_constant('I_Na_Markov.conc', self.spinAADConcentration.value() / 1e6)
                else:
                    s.set_constant('I_Na_Markov.conc', 0)
                
                progrep.msgvar = "Model 2 - With Blocker -"
                s.pre(prebeats*bcl, progress=progrep)
                data2_temp = s.run(showbeats*bcl, progress=progrep, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                data2.append(data2_temp)
                apds2_alt = data2_temp.apd(v='output.Vm', threshold=0.9*np.min(data2_temp['output.Vm']))
                CaT2_alt = np.max(data2_temp['output.Cai']) - np.min(data2_temp['output.Cai'])
                #Syst2_alt = np.max(data2_temp['output.Cai'])
                #Diast2_alt = np.min(data2_temp['output.Cai'])            
                dvdt2_alt = np.diff(data2_temp['output.Vm']) / np.diff(data2_temp[model2.time()])
                dvdtmax2_alt = np.max(dvdt2_alt)                     
                if len(apds2_alt) > 0:
                    self.lblAPDCaTModel2Alt.setText("%s\n %.1f Hz AAD1 - APD: %d ms // dV/dt_max: %d mV/ms // CaT: %d nM" % (self.lblAPDCaTModel2Alt.text(), (1000/bcl), apds2_alt['duration'][0], dvdtmax2_alt, 1000*CaT2_alt))
                else:
                    self.lblAPDCaTModel2Alt.setText("%s\n %.1f Hz AAD1 - APD: ? ms // dV/dt_max: ? mV/ms // CaT: ? nM" % (self.lblAPDCaTModel2Alt.text()), (1000/bcl))            
                
                if self.checks1s2_mdl2.isChecked():
                    peakrefval = np.max(data2_temp['output.Vm'])
                    ERP_ref = 0                      
                    state = s.state()
                    print("Running S1S2 protocol - AAD1:Model2")
                    for ks2, cur_s1s2 in enumerate(s1s2_2):
                        p2 = myokit.Protocol()
                        p2.schedule(stimamp,10,stimdur,bcl,0) 
                        p2.schedule(stimamp,10+float(cur_s1s2),stimdur,bcl,1)
                        s.set_protocol(p2)
                        s.reset() 
                        s.set_state(state)
                        d2 = s.run(bcl, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                        data2.append(d2)

                        d_trim = d2.trim_left(0.75 * apds2_alt['duration'][0])#apds1_s1s2[0][1])
                        peakval = np.max(d_trim['output.Vm'])
                        if peakval > 0.8*peakrefval and ERP_ref == 0:
                            ERP_ref = float(cur_s1s2)
                    
                    self.lblAPDCaTModel2Alt.setText("%s\n AAD1 - ERP: %d ms" % (self.lblAPDCaTModel2Alt.text(), ERP_ref))

                s = myokit.Simulation(model2, p)
                s.set_constant('parameters.Ca_o', self.spinCao2.value())
                s.set_constant('parameters.K_o', self.spinKo2.value())
                s.set_constant('parameters.Na_o', self.spinNao2.value())  
                
                s.set_constant('parameters.ICaL_Block', self.spinICaL_2.value() / 100.0)
                s.set_constant('parameters.IK1_Block', self.spinIK1_2.value() / 100.0)
                s.set_constant('parameters.IKr_Block', self.spinIKr_2.value() / 100.0)
                s.set_constant('parameters.IKs_Block', self.spinIKs_2.value() / 100.0)
                s.set_constant('parameters.IKur_Block', self.spinIKur_2.value() / 100.0)
                s.set_constant('parameters.INa_Block', self.spinINa_2.value() / 100.0)
                s.set_constant('parameters.INaL_Block', self.spinINaL_2.value() / 100.0)
                s.set_constant('parameters.INaK_Block', self.spinINaK_2.value() / 100.0)
                s.set_constant('parameters.INCX_Block', self.spinINCX_2.value() / 100.0)
                s.set_constant('parameters.Ito_Block', self.spinIto_2.value() / 100.0)
                s.set_constant('I_Na_Markov.new_drug_mode', 0)
                
                if self.cmbAAD_3.currentText()=='Flecainide': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 3)
                elif self.cmbAAD_3.currentText()=='Lidocaine': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 2)
                elif self.cmbAAD_3.currentText()=='Vernakalant': 
                    s.set_constant('I_Na_Markov.class1_drug_cat', 4)
    
                if self.markov_2.isChecked() == True:
                    s.set_constant('I_Na_Markov.conc', self.spinAADConcentration_3.value() / 1e6)
                else:
                    s.set_constant('I_Na_Markov.conc', 0)
                
                progrep.msgvar = "Model 2 - With Another Blocker -"
                s.pre(prebeats*bcl, progress=progrep)
                data2b_temp = s.run(showbeats*bcl, progress=progrep, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                data2b.append(data2b_temp)
                apds2b_alt = data2b_temp.apd(v='output.Vm', threshold=0.9*np.min(data2b_temp['output.Vm']))
                CaTb_alt = np.max(data2b_temp['output.Cai']) - np.min(data2b_temp['output.Cai'])   
                #Syst2b_alt = np.max(data2b_temp['output.Cai'])
                #Diast2b_alt = np.min(data2b_temp['output.Cai'])                     
                dvdt2b_alt = np.diff(data2b_temp['output.Vm']) / np.diff(data2b_temp[model2.time()])
                dvdtmax2b_alt = np.max(dvdt2b_alt)                       
                if len(apds2b_alt) > 0:
                    self.lblAPDCaTModel2Alt_2.setText("%s\n %.1f Hz AAD2 - APD: %d ms // dV/dt_max: %d mV/ms // CaT: %d nM" % (self.lblAPDCaTModel2Alt_2.text(), (1000/bcl), apds2b_alt['duration'][0], dvdtmax2b_alt, 1000*CaTb_alt))
                else:
                    self.lblAPDCaTModel2Alt_2.setText("%s\n %.1f Hz AAD2 - APD: ? ms // dV/dt_max: ? mV/ms // CaT: ? nM" % (self.lblAPDCaTModel2Alt_2.text()), (1000/bcl))            
                
                if self.checks1s2_mdl2.isChecked():
                    peakrefval = np.max(data2b_temp['output.Vm'])
                    ERP_ref = 0                           
                    state = s.state()
                    print("Running S1S2 protocol - AAD2:Model2")
                    #data= np.zeros(100)
                    for ks2, cur_s1s2 in enumerate(s1s2_2):
                        p2 = myokit.Protocol()
                        p2.schedule(stimamp,10,stimdur,bcl,0) 
                        p2.schedule(stimamp,10+float(cur_s1s2),stimdur,bcl,1)
                        s.set_protocol(p2)
                        s.reset() 
                        s.set_state(state)
                        d2 = s.run(bcl, log=myokit.LOG_STATE+myokit.LOG_INTER+myokit.LOG_BOUND)
                        data2b.append(d2)                

                        d_trim = d2.trim_left(0.75 * apds2b_alt['duration'][0])#apds1_s1s2[0][1])
                        peakval = np.max(d_trim['output.Vm'])
                        if peakval > 0.8*peakrefval and ERP_ref == 0:
                            ERP_ref = float(cur_s1s2)
                    
                    self.lblAPDCaTModel2Alt_2.setText("%s\n AAD2 - ERP: %d ms" % (self.lblAPDCaTModel2Alt_2.text(), ERP_ref))
                            
                #if len(self.cmbOutput2Top.currentText()) > 1:
                #    self.mplOutput2Top.axes.plot(data2_ref[model2.time()],data2_ref[self.cmbOutput2Top.currentText()],'-k', data2[model2.time()],data2[self.cmbOutput2Top.currentText()],'-r', data2b[model2.time()],data2b[self.cmbOutput2Top.currentText()],'-b', data2_ref_r2[model2.time()],data2_ref_r2[self.cmbOutput2Top.currentText()],':k', data2_r2[model2.time()],data2_r2[self.cmbOutput2Top.currentText()],':r', data2b_r2[model2.time()],data2b_r2[self.cmbOutput2Top.currentText()],':b', data2_ref_r3[model2.time()],data2_ref_r3[self.cmbOutput2Top.currentText()],'-.k', data2_r3[model2.time()],data2_r3[self.cmbOutput2Top.currentText()],'-.r', data2b_r3[model2.time()],data2b_r3[self.cmbOutput2Top.currentText()],'-.b')
                #    self.mplOutput2Top.draw()
                #    self.mplOutput2Bottom.axes.plot(data2_ref[model2.time()],data2_ref[self.cmbOutput2Bottom.currentText()],'-k', data2[model2.time()],data2[self.cmbOutput2Bottom.currentText()],'-r', data2b[model2.time()],data2b[self.cmbOutput2Bottom.currentText()],'-b', data2_ref_r2[model2.time()],data2_ref_r2[self.cmbOutput2Bottom.currentText()],':k', data2_r2[model2.time()],data2_r2[self.cmbOutput2Bottom.currentText()],':r', data2b_r2[model2.time()],data2b_r2[self.cmbOutput2Bottom.currentText()],':b', data2_ref_r3[model2.time()],data2_ref_r3[self.cmbOutput2Bottom.currentText()],'-.k', data2_r3[model2.time()],data2_r3[self.cmbOutput2Bottom.currentText()],'-.r', data2b_r3[model2.time()],data2b_r3[self.cmbOutput2Bottom.currentText()],'-.b')
                #    self.mplOutput2Bottom.draw()
    
            if len(self.cmbOutput2Top.currentText()) > 1:
                self.mplOutput2Top.axes.hold(True)
                self.mplOutput2Bottom.axes.hold(True)
                for k, item in enumerate(data2):
                    data2_temp = data2[k]
                    data2b_temp = data2b[k]
                    data2_ref_temp = data2_ref[k] 
                    if self.aad1_mdl2_top.isChecked():
                        self.mplOutput2Top.axes.plot(data2_temp[model2.time()],data2_temp[self.cmbOutput2Top.currentText()],'-r')
                    if self.aad2_mdl2_top.isChecked():
                        self.mplOutput2Top.axes.plot(data2b_temp[model2.time()],data2b_temp[self.cmbOutput2Top.currentText()],'-b')
                    if self.ref_mdl2_top.isChecked():
                        self.mplOutput2Top.axes.plot(data2_ref_temp[model2.time()],data2_ref_temp[self.cmbOutput2Top.currentText()],'-k')
                    if self.aad1_mdl2_bottom.isChecked():
                        self.mplOutput2Bottom.axes.plot(data2_temp[model2.time()],data2_temp[self.cmbOutput2Bottom.currentText()],'-r')
                    if self.aad2_mdl2_bottom.isChecked():
                        self.mplOutput2Bottom.axes.plot(data2b_temp[model2.time()],data2b_temp[self.cmbOutput2Bottom.currentText()],'-b')
                    if self.ref_mdl2_bottom.isChecked():
                        self.mplOutput2Bottom.axes.plot(data2_ref_temp[model2.time()],data2_ref_temp[self.cmbOutput2Bottom.currentText()],'-k')
                self.mplOutput2Top.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())
                self.mplOutput2Bottom.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())
                self.mplOutput2Top.draw()                
                self.mplOutput2Bottom.draw()

    def yaxis_equalizer(self):            
        if self.chkEqualYAxis.isChecked():
            #Top:
            yrmdl1 = self.mplOutput1Top.axes.get_ylim()
            yrmdl2 = self.mplOutput2Top.axes.get_ylim()
            
            yrmdllow = yrmdl1[0]
            if yrmdl2[0] < yrmdl1[0]:
                yrmdllow = yrmdl2[0]

            yrmdlhigh = yrmdl1[1]                                   
            if yrmdl2[1] > yrmdl1[1]:
                yrmdlhigh = yrmdl2[1]

            self.mplOutput1Top.axes.set_ylim(yrmdllow, yrmdlhigh, auto=False)
            self.mplOutput1Top.draw()
            self.mplOutput2Top.axes.set_ylim(yrmdllow, yrmdlhigh, auto=False)
            self.mplOutput2Top.draw()
            
            #Bottom:
            yrmdl1 = self.mplOutput1Bottom.axes.get_ylim()
            yrmdl2 = self.mplOutput2Bottom.axes.get_ylim()
            
            yrmdllow = yrmdl1[0]
            if yrmdl2[0] < yrmdl1[0]:
                yrmdllow = yrmdl2[0]

            yrmdlhigh = yrmdl1[1]                                   
            if yrmdl2[1] > yrmdl1[1]:
                yrmdlhigh = yrmdl2[1]

            self.mplOutput1Bottom.axes.set_ylim(yrmdllow, yrmdlhigh, auto=False)
            self.mplOutput1Bottom.draw()
            self.mplOutput2Bottom.axes.set_ylim(yrmdllow, yrmdlhigh, auto=False)
            self.mplOutput2Bottom.draw()
    
    def plotselection(self):
        global data1_ref, data1, data1b
        global data2_ref, data2, data2b
        
        if len(self.cmbOutput1Top.currentText()) > 1:
            self.mplOutput1Top.axes.clear()
            self.mplOutput1Bottom.axes.clear()          
            self.mplOutput1Top.axes.hold(True)
            self.mplOutput1Bottom.axes.hold(True)
            for k, item in enumerate(data1):
                data1_temp = data1[k]
                data1b_temp = data1b[k]
                data1_ref_temp = data1_ref[k] 
                if self.aad1_mdl1_top.isChecked():
                    self.mplOutput1Top.axes.plot(data1_temp[model1.time()],data1_temp[self.cmbOutput1Top.currentText()],'-r')
                if self.aad2_mdl1_top.isChecked():
                    self.mplOutput1Top.axes.plot(data1b_temp[model1.time()],data1b_temp[self.cmbOutput1Top.currentText()],'-b')
                if self.ref_mdl1_top.isChecked():
                    self.mplOutput1Top.axes.plot(data1_ref_temp[model1.time()],data1_ref_temp[self.cmbOutput1Top.currentText()],'-k')
                if self.aad1_mdl1_bottom.isChecked():
                    self.mplOutput1Bottom.axes.plot(data1_temp[model1.time()],data1_temp[self.cmbOutput1Bottom.currentText()],'-r')
                if self.aad2_mdl1_bottom.isChecked():
                    self.mplOutput1Bottom.axes.plot(data1b_temp[model1.time()],data1b_temp[self.cmbOutput1Bottom.currentText()],'-b')
                if self.ref_mdl1_bottom.isChecked():
                    self.mplOutput1Bottom.axes.plot(data1_ref_temp[model1.time()],data1_ref_temp[self.cmbOutput1Bottom.currentText()],'-k')
            self.mplOutput1Top.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())
            self.mplOutput1Bottom.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())
            self.mplOutput1Top.draw()                
            self.mplOutput1Bottom.draw()        

        if len(self.cmbOutput2Top.currentText()) > 1:
            self.mplOutput2Top.axes.clear()
            self.mplOutput2Bottom.axes.clear()
            self.mplOutput2Top.axes.hold(True)
            self.mplOutput2Bottom.axes.hold(True)
            for k, item in enumerate(data2):
                data2_temp = data2[k]
                data2b_temp = data2b[k]
                data2_ref_temp = data2_ref[k] 
                if self.aad1_mdl2_top.isChecked():
                    self.mplOutput2Top.axes.plot(data2_temp[model2.time()],data2_temp[self.cmbOutput2Top.currentText()],'-r')
                if self.aad2_mdl2_top.isChecked():
                    self.mplOutput2Top.axes.plot(data2b_temp[model2.time()],data2b_temp[self.cmbOutput2Top.currentText()],'-b')
                if self.ref_mdl2_top.isChecked():
                    self.mplOutput2Top.axes.plot(data2_ref_temp[model2.time()],data2_ref_temp[self.cmbOutput2Top.currentText()],'-k')
                if self.aad1_mdl2_bottom.isChecked():
                    self.mplOutput2Bottom.axes.plot(data2_temp[model2.time()],data2_temp[self.cmbOutput2Bottom.currentText()],'-r')
                if self.aad2_mdl2_bottom.isChecked():
                    self.mplOutput2Bottom.axes.plot(data2b_temp[model2.time()],data2b_temp[self.cmbOutput2Bottom.currentText()],'-b')
                if self.ref_mdl2_bottom.isChecked():
                    self.mplOutput2Bottom.axes.plot(data2_ref_temp[model2.time()],data2_ref_temp[self.cmbOutput2Bottom.currentText()],'-k')
            self.mplOutput2Top.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())
            self.mplOutput2Bottom.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())
            self.mplOutput2Top.draw()                
            self.mplOutput2Bottom.draw()

    def xaxis_adjustment1(self): 
        self.mplOutput1Top.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())
        self.mplOutput1Top.draw()
        self.mplOutput1Bottom.axes.set_xlim(self.xaxis_mdl1_from.value(), self.xaxis_mdl1_to.value())
        self.mplOutput1Bottom.draw()
            
    def xaxis_adjustment2(self):
        self.mplOutput2Top.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())
        self.mplOutput2Top.draw()
        self.mplOutput2Bottom.axes.set_xlim(self.xaxis_mdl2_from.value(), self.xaxis_mdl2_to.value())
        self.mplOutput2Bottom.draw()
            
    def resetaxes(self):
        self.xaxis_mdl1_from.setValue(0)
        self.xaxis_mdl1_to.setValue(1000)
        self.xaxis_mdl2_from.setValue(0) 
        self.xaxis_mdl2_to.setValue(1000)
            
    def savecsv1(self):
        global model1, data1, data1_ref, data1b

        export_mdl1 = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', "CSV (*.csv);;Text (*.txt);;All Files (*.*)")
        ext1 = export_mdl1[len(export_mdl1)-4:len(export_mdl1)]
        export_mdl1_top = export_mdl1[:(len(export_mdl1)-4)]+"_Top"+ext1
        
        with open(export_mdl1_top,'wb') as f1_top:
            for k, item in enumerate(data1):
                #print(k)
                data1_temp = data1[k]
                data1b_temp = data1b[k]
                data1_ref_temp = data1_ref[k] 
                max_length = np.max([len(data1_ref_temp[model1.time()]),len(data1_temp[model1.time()]),len(data1b_temp[model1.time()])])
                time1_ref_temp = np.concatenate((data1_ref_temp[model1.time()], np.zeros(max_length-len(data1_ref_temp[model1.time()])+1)))
                time1_temp = np.concatenate((data1_temp[model1.time()], np.zeros(max_length-len(data1_temp[model1.time()])+1)))
                time1b_temp = np.concatenate((data1b_temp[model1.time()], np.zeros(max_length-len(data1b_temp[model1.time()])+1)))
                val1_ref_temp = np.concatenate((data1_ref_temp[self.cmbOutput1Top.currentText()], np.zeros(max_length-len(data1_ref_temp[self.cmbOutput1Top.currentText()])+1)))
                val1_temp = np.concatenate((data1_temp[self.cmbOutput1Top.currentText()], np.zeros(max_length-len(data1_temp[self.cmbOutput1Top.currentText()])+1)))
                val1b_temp = np.concatenate((data1b_temp[self.cmbOutput1Top.currentText()], np.zeros(max_length-len(data1b_temp[self.cmbOutput1Top.currentText()])+1)))
                np.savetxt(f1_top, np.c_[time1_ref_temp, val1_ref_temp, time1_temp, val1_temp, time1b_temp, val1b_temp], delimiter=',', footer='\n\n')
               
                #np.savetxt(f1_top, np.c_[data1_ref_temp[model1.time()], data1_ref_temp[self.cmbOutput1Top.currentText()], data1_temp[self.cmbOutput1Top.currentText()], data1b_temp[self.cmbOutput1Top.currentText()]], delimiter=',')

        export_mdl1_bottom = export_mdl1[:(len(export_mdl1)-4)]+"_Bottom"+ext1
       
        with open(export_mdl1_bottom,'wb') as f1_bottom:
            for k, item in enumerate(data1):
                data1_temp = data1[k]
                data1b_temp = data1b[k]
                data1_ref_temp = data1_ref[k] 
                max_length = np.max([len(data1_ref_temp[model1.time()]),len(data1_temp[model1.time()]),len(data1b_temp[model1.time()])])
                time1_ref_temp = np.concatenate((data1_ref_temp[model1.time()], np.zeros(max_length-len(data1_ref_temp[model1.time()])+1)))
                time1_temp = np.concatenate((data1_temp[model1.time()], np.zeros(max_length-len(data1_temp[model1.time()])+1)))
                time1b_temp = np.concatenate((data1b_temp[model1.time()], np.zeros(max_length-len(data1b_temp[model1.time()])+1)))
                val1_ref_temp = np.concatenate((data1_ref_temp[self.cmbOutput1Bottom.currentText()], np.zeros(max_length-len(data1_ref_temp[self.cmbOutput1Bottom.currentText()])+1)))
                val1_temp = np.concatenate((data1_temp[self.cmbOutput1Bottom.currentText()], np.zeros(max_length-len(data1_temp[self.cmbOutput1Bottom.currentText()])+1)))
                val1b_temp = np.concatenate((data1b_temp[self.cmbOutput1Bottom.currentText()], np.zeros(max_length-len(data1b_temp[self.cmbOutput1Bottom.currentText()])+1)))
                np.savetxt(f1_bottom, np.c_[time1_ref_temp, val1_ref_temp, time1_temp, val1_temp, time1b_temp, val1b_temp], delimiter=',', footer='\n\n')
    
                #np.savetxt(f1_bottom, np.c_[data1_ref_temp[model1.time()], data1_ref_temp[self.cmbOutput1Bottom.currentText()], data1_temp[self.cmbOutput1Bottom.currentText()], data1b_temp[self.cmbOutput1Bottom.currentText()]], delimiter=',')

    def savecsv2(self):
        global model2, data2, data2_ref, data2b
        
        export_mdl2 = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', "CSV (*.csv);;Text (*.txt);;All Files (*.*)")
        ext2 = export_mdl2[len(export_mdl2)-4:len(export_mdl2)]
        export_mdl2_top = export_mdl2[:(len(export_mdl2)-4)]+"_Top"+ext2

        with open(export_mdl2_top,'wb') as f2_top:
            for k, item in enumerate(data2):
                data2_temp = data2[k]
                data2b_temp = data2b[k]
                data2_ref_temp = data2_ref[k] 

                max_length = np.max([len(data2_ref_temp[model2.time()]),len(data2_temp[model2.time()]),len(data2b_temp[model2.time()])])
                time2_ref_temp = np.concatenate((data2_ref_temp[model2.time()], np.zeros(max_length-len(data2_ref_temp[model2.time()])+1)))
                time2_temp = np.concatenate((data2_temp[model2.time()], np.zeros(max_length-len(data2_temp[model2.time()])+1)))
                time2b_temp = np.concatenate((data2b_temp[model2.time()], np.zeros(max_length-len(data2b_temp[model2.time()])+1)))
                val2_ref_temp = np.concatenate((data2_ref_temp[self.cmbOutput2Top.currentText()], np.zeros(max_length-len(data2_ref_temp[self.cmbOutput2Top.currentText()])+1)))
                val2_temp = np.concatenate((data2_temp[self.cmbOutput2Top.currentText()], np.zeros(max_length-len(data2_temp[self.cmbOutput2Top.currentText()])+1)))
                val2b_temp = np.concatenate((data2b_temp[self.cmbOutput2Top.currentText()], np.zeros(max_length-len(data2b_temp[self.cmbOutput2Top.currentText()])+1)))
                np.savetxt(f2_top, np.c_[time2_ref_temp, val2_ref_temp, time2_temp, val2_temp, time2b_temp, val2b_temp], delimiter=',', footer='\n\n')

                #np.savetxt(f2_top, np.c_[data2_ref_temp[model2.time()], data2_ref_temp[self.cmbOutput2Top.currentText()], data2_temp[self.cmbOutput2Top.currentText()], data2b_temp[self.cmbOutput2Top.currentText()]], delimiter=',')

        export_mdl2_bottom = export_mdl2[:(len(export_mdl2)-4)]+"_Bottom"+ext2
      
        with open(export_mdl2_bottom,'wb') as f2_bottom:
            for k, item in enumerate(data2):
                data2_temp = data2[k]
                data2b_temp = data2b[k]
                data2_ref_temp = data2_ref[k] 

                max_length = np.max([len(data2_ref_temp[model2.time()]),len(data2_temp[model2.time()]),len(data2b_temp[model2.time()])])
                time2_ref_temp = np.concatenate((data2_ref_temp[model2.time()], np.zeros(max_length-len(data2_ref_temp[model2.time()])+1)))
                time2_temp = np.concatenate((data2_temp[model2.time()], np.zeros(max_length-len(data2_temp[model2.time()])+1)))
                time2b_temp = np.concatenate((data2b_temp[model2.time()], np.zeros(max_length-len(data2b_temp[model2.time()])+1)))
                val2_ref_temp = np.concatenate((data2_ref_temp[self.cmbOutput2Bottom.currentText()], np.zeros(max_length-len(data2_ref_temp[self.cmbOutput2Bottom.currentText()])+1)))
                val2_temp = np.concatenate((data2_temp[self.cmbOutput2Bottom.currentText()], np.zeros(max_length-len(data2_temp[self.cmbOutput2Bottom.currentText()])+1)))
                val2b_temp = np.concatenate((data2b_temp[self.cmbOutput2Bottom.currentText()], np.zeros(max_length-len(data2b_temp[self.cmbOutput2Bottom.currentText()])+1)))
                np.savetxt(f2_bottom, np.c_[time2_ref_temp, val2_ref_temp, time2_temp, val2_temp, time2b_temp, val2b_temp], delimiter=',', footer='\n\n')
    
                #np.savetxt(f2_bottom, np.c_[data2_ref_temp[model2.time()], data2_ref_temp[self.cmbOutput2Bottom.currentText()], data2_temp[self.cmbOutput2Bottom.currentText()], data2b_temp[self.cmbOutput2Bottom.currentText()]], delimiter=',')

    
class MyokitProgressReporter(myokit.ProgressReporter):
    target = None
    msgvar = None
    def __init__(self, tar=None):
        self.target = tar
        
    def enter(self, msg=None):        
        print("Starting sim...")

    def exit(self):
        #self.target.clearMessage()
        print("Done!")
    
    def update(self, progress):
        val = progress * 100.0
        #print("Progress = " + str(progress))
        #self.target.setValue(int(val))
        self.target.showMessage(self.msgvar + " Progress: " + str(val) + "%", 2000);
        
        QtWidgets.QApplication.processEvents(QtCore.QEventLoop.ExcludeUserInputEvents)
        return True
        
def run():
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()

run()
