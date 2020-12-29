#!/usr/bin/env python3
import os
import sys
import time
import re
import subprocess
from datetime import datetime


def clear_screen() :        
	'''for clearing screen'''
	if os.name == 'nt' :          #For Windows
		_ = os.system('cls')
	else :                     #For Linux and Mac
		_ = os.system('clear')


def package_check() :               
	'''for installing uninstalled packages'''
	try :
		import numpy as np
	except ImportError as e :
		print('\nNumpy package is not installed. Installing Numpy package\n')
		time.sleep(1.5)
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
	
	try :
		import pandas 
	except ImportError as e :
		print('\nPandas package is not installed. Installing Pandas package\n')
		time.sleep(1.5)
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas==1.0.1']) #using older version cause the new version is causing problems in Windows
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'plotting'])

	try :
		import openpyxl
	except ImportError as e :
		print('\nOpenpyxl package is not installed. Installing openpyxl package\n')
		time.sleep(1.5)
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openpyxl'])

	try :
		import textwrap
	except ImportError as e :
		print('\nTabulate package is not installed. Installing tabulate package\n')
		time.sleep(1.5)
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'textwrap3'])

	print('\n\nAll packages ready to use ' + '\U0001f600')
	time.sleep(1.5)
	
	
def run_count() :
	'''counts the number of logins'''
	_here = os.path.dirname(os.path.abspath(__file__))
	filename = os.path.join(_here, 'report_index.csv')
	
	if os.path.isfile(filename) :  #if the file already exists i.e. the program is not running for the first time
		data = pd.read_csv(filename)
		data['Values'][0] = eval(str(data['Values'][0])) + 1           #increasing the program run counter
		data.to_csv(filename, index=False)
	else :
		a = ['Total time program ran', 'Reports_saved', '', 'Reports']
		b = [1, 0, '', '']
		c = ['', '', '', '']
		pd.DataFrame({'Description' : a, 'Values' : b, 'Timestamp' : c, 'Comment' : c}).to_csv(filename, index=False)
	
	
def report_index(report_name, report_path, comments) :
	#creates a record when a new report is created
	_here = os.path.dirname(os.path.abspath(__file__))
	filename = os.path.join(_here, 'report_index.csv')
	
	data = pd.read_csv(filename)
	data['Values'][1] = eval(str(data['Values'][1])) + 1     #increasing the reports_saved counter
	data_new = data.append(pd.DataFrame({'Description' : [report_name], 'Values' : [report_path], 'Timestamp' : [datetime.now()], 'Comment' : [comments]}))
	data_new.to_csv(filename, index=False)


def instructions() :                   
	'''instructions section'''
	print('~'*150 + '\n\t\t\tINSTRUCTIONS  ' +  '\U0001F4D4'+ '\n' + '~'*150)
	print('\n')
	print('''INPUTS:
1. Enter the values only in the instructed units only.
2. If the water table lies inside a soil layer, PROVIDE THE LAYER AS TWO DIFFERENT LAYERS, the one above the water table with bulk unit weight, and the one below with saturated unit weight.
Example: Assume a system with 3 layers of with depth 3m, 6m and 5m respectively. The water table is at a depth of 5m below ground level i.e. lying in second soil layers. So instead of providing 3 layers, provide 4 layers with depth 3m, 2m, 4m and 5m. Provide bulk unit weight for 2 layers above the water table and saturated unit weight for 2 layers below W.T.
\nASSUMPTIONS MADE :
1. Critical depth for Loose sand = 15*D\t Dense sand = 20*D
2. Effective overburden pressure at effective depth * Nq < 11000 kN/m^2. If found higher, use 11000 kN/m^2
3. Skin friction pressure < 100 kN/m^2. If found higher, use 100 kN/m^2
4. For loose sand, K=1 \t Dense sand, K=2
\nREPORT :
1. Report will contain all the inputs, the values calculated and final results.
2. The report will be saved in the very folder where this program file is saved.
3. The report will be saved in .xlsx format by default. To save in the csv format, specifically provide the .csv extension in the filename.
Example : if 'report' is provided as the filename, it will be saved as report.xlsx by default. Provide 'report.csv' to save as a csv file.
4. Values for different layers will be in form of lists. For instance, if 5m, 7m and 6m are depth corresponding to 1st, 2nd and 3rd layer, it will be stored as [5,7,6].
5. Values like cohesion will be stored as NAN for loose and dense sand. Similarly values like angle of internal friction will be NAN for clayey layer..
\nREPORT INDEX :
1. This is a csv file that keeps a record of total saved report files, their location with timestamps.
2. This file also keeps a track of how many times the program was run plus total number of reports saved.
3. This file DOES NOT update when a report is deleted or moved from its actual location, but a deleted report is not displayed in the Report Index menu.
4. It is available in the same folder where this script is saved.
5. Record index option available on the main screen can be used to look into the file from the program itself.
		  ''')
	_ = input('\nPress Enter to go back   ')
	main_screen()
	
		  
def about_us() :                 
	'''about us section'''
	print('~'*150 + '\n\t\t\tABOUT DEVS   ' + '\U0001F4BB' + '\n' + '~'*150)
	print('\n')
	print('''
\nThis program is developed by five undergrads from Civil Engineering Department, NIT Trichy.
1. Ayush Kumar Singh (103117024)
2. Ashish (103117018)
3. Amit Sharma (103117012)
4. Munindar Jivaram Ahir (103117060)
5. Utkarsh Raj Atri (103117100)
\nIt took days to write and debug the code. The code follows IS 2911-2010 guidelines and specifications.\n
\nIt is an open source code and is freely available to modify and rectify.
\nContact details of developers:
Ayush : ayush.rlb1999@gmail.com
Ashish : ashish17032001@gmail.com
Amit : amitsharma1201486@gmail.com
Munindar : munindarahir231@gmail.com
Utkarsh : utkarshrajatri@gmail.com
	      ''')
	_ = input('\n\nPress Enter to go back')
	main_screen()
	
	
def computation() :  
	'''Actual Computation takes place here'''
	try :              
		print('~'*150 + '\n\t\t\tBEARING CAPACITY OF PILES   ' + '\U0001F3CB' +'\n' + '~'*150 )

		method = int(input('Which method to follow? \n1. Static Analysis\n2. Use of SPT data (for bored piles)\t'))

		if method == 2 :  #SPT method
			#As per Clause B-4.1 and B-4.2 Page 12
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#INPUT
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			soil_type = int(input('\nSoil type (1. Cohesionless soil, 2. Non-plastic silt or very fine sand) : '))
			shape = int(input('Shape of the pile (1. Square,  2. Circular) : '))
			L = float(input('Length of penetration of pile in the bearing strata (in m) : '))
			size = float(input('Side (in m) :')) if shape == 1 else float(input('Radius (in m) : '))
			Ep = float(input('Elastic modulus of pile material (in N/mm^2) : ')) * 10**6
			Es = float(input('Modulus of Elasticity of soil at or below the pile point (N/mm^2): ')) * 10**6
			mu_s = float(input('Poisson\'s ratio of soil : '))
			N = float(input('Average N value at pile tip : '))
			N_bar = float(input('Average N along the pile shaft : '))
			fos = float(input('Factor of Safety : '))

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#CALCULATION
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			x = np.min([10*L/size if soil_type==2 else 13*L/size, 130]) #the end bearing resistance should not exceed 130NAp. 
			area = size**2 if shape==1 else np.pi*size*size/4  #cross-sectional area of pile tip
			surface_area = 4*L*size if shape ==1 else np.pi*size*L   #surface area of pile shaft
			denominator = 0.6 if soil_type==2 else 0.5

			Qb = (x*N*area)  #end bearing resistance
			Qs = (N_bar * surface_area)/denominator   #skin friction resistance
			Qup = np.round(Qb + Qs, 5)          #ultimate load capacity
			Qap = np.round(Qup / fos, 5)    #allowable load capacity

		
		else :	#for Static Analysis
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#INPUT
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

			print('\nPILE INFO')
			pile_type = int(input('\nEnter the type of pile (1. Driven  2. Bored) : '))
			shape = int(input('Enter the shape of pile (1. Square  2. Circular) : '))
			size = float(input('Size of pile (in m) : '))
			Ep = float(input('Elastic modulus of pile material (in N/mm^2) : ')) * 10**6

			print('\nSOIL INFO')
			phi_last = float(input('Angle of internal friction for last layer (deg): '))      #angle of internal friction for last layer
			Es = float(input('Modulus of Elasticity of soil at or below the pile point (N/mm^2) : ')) * 10**6
			mu_s = float(input('Poisson\'s ratio of soil : '))
			fos = float(input('Factor of Safety : '))
			#these are for last layer
			i = np.pi/4 + np.radians(phi_last)/2
			Nq = ((np.tan(i))**2)*np.exp(np.pi * np.tan(np.radians(phi_last)))
			N_gamma = 2*(Nq+1)*np.tan(np.radians(phi_last))
			Nc = (Nq-1)/np.tan(np.radians(phi_last))

			n_layers = int(input('Number of layers : '))

			gamma_t = []       #unit weight of soil
			layer_type = []     #layer type
			phi = []    #angle of internal friction
			h1, h = [], []       #length of pile in each layer
			alpha = []
			cu = []

			for i in range(n_layers) :
				print('\nLayer' + str(i+1) + ' : ')
				layer_type.append(int(input('Soil type (1.Loose sand   2.Dense sand   3.Clayey) : ')))
				gamma_t.append(float(input('Unit weight of soil (kN/m^3) (If below water table, then saturated unit weight): ')))
				h1.append(float(input('Length of pile in the layer (m) : ')))
				if layer_type[i] == 3 :
					cu.append(float(input('Cu (kN/m^2) : ')))
					alpha.append(float(input('Adhesion factor : ')))
					phi.append(np.nan)
				else :
					alpha.append(np.nan)          #Sand doesn't have Adhesion factor
					cu.append(np.nan)
					phi.append(float(input('Angle of internal friction (deg): ')))

			wt = float(input('\nDepth of water table (m) : '))

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#COMPUTATION STARTS
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#SAFE LOAD CALCULATION
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

			#converting every list into array
			gamma_t, phi, h1, alpha, cu = np.array(gamma_t), np.array(phi), np.array(h1), np.array(alpha), np.array(cu)
			#N_gamma

			L = np.sum(h1)		#actual total length of pile
			#critical depth calculation
			for i in range(n_layers) :
				cd = 15*size if layer_type==1 else 20*size if layer_type==2 else h1[i]    #finding critical depth for sand
				h.append(cd if cd < h1[i] else h1[i])       #if critical depth less than actual depth, replace it with critical depth
				
			h = np.array(h)
			area = size ** 2 if shape == 1 else np.pi*size*size/4   #finding area of the tip of pile
			sai = 4*size*h if shape==1 else np.pi*size*h     #surface area of each section of the pile
			
			#effective overburden pressure calculation
			h_wt = np.sum(h)-wt if wt < np.sum(h) else 0   #if water table is actually much below the total pile depth, then it's of no use.
			sigma_net = np.sum(gamma_t * h) - 9.81 * h_wt   #this all is valid if the lowest soil strata is granular
			
			#end-bearing pressure if granular soil at pile tip
			qu = np.min([sigma_net*Nq + 0.5*size*gamma_t[-1]*N_gamma , 11000])  #if qu = sigma_net*Nq > 11000, then qu = 11000 kN/m^2
			
			#end-bearing pressure if strata at pile tip is cohesive
			if layer_type[-1] == 3 :
				qu = np.min([area * Nc * cu[-1], 11000])
			
			#end-bearing capacity	
			Qb = qu*area if pile_type==1 else 0.5*qu*area  #Qb for bored pile = 0.5*Qb for driven pile

			#Skin friction 
			qi = []
			for i in range(n_layers) :
				if layer_type[i] == 3 :        #for clay
					qi.append(alpha[i]*cu[i]*sai[i])
				else :                         #for sand
					k = 1 if layer_type[i] == 1 else 2
					delta = np.radians(0.75*phi[i])    #finding del and converting to radians
					sigma_s = np.sum(gamma_t[:i]*h[:i]) - 9.81*np.max([np.sum(h[:i])-wt, 0]) if i>0 else 0
					#if water table is below the current layer, the difference will be negative and max will be taken as 0.
					sigma_end = np.sum(gamma_t[:i+1]*h[:i+1]) - 9.81*np.max([np.sum(h[:i+1])-wt, 0])
					sigma_avg = (sigma_s + sigma_end)/2      
					qs = np.min([k*sigma_avg*np.tan(delta), 100])     #if qs > 100, then qs = 100 kN/m^2
					qi.append(qs*sai[i])

			Qs = np.sum(np.array(qi))
			Qup = Qb + Qs    #ultimate load capacity
			Qup = np.round(Qup, 5)
			Qap = np.round(Qup / fos, 5)    #allowable load capacity


		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		#SETTLEMENT CALCULATION
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		dist_type = int(input('Nature of skin friction resistance distribution along the pile shaft (1. Uniform or Parabolic, 2. Triangular) : '))
		E = 0.67 if dist_type == 2 else 0.5      #Vesic 1977
		Iwp = 0.85  #influence factor for Se2
		Iws = 2 + 0.35 * (L / size)**0.5   #influence factor for Se3
		perimeter = 4*size if shape == 1 else np.pi * size #perimeter of the pile tip

		Se1 = ( (Qb/fos) + E*(Qs/fos) )*L / (area * Ep)   #Settlement of pile shaft
		Se2 = ( (Qb/fos) * size) * (1- mu_s**2)* Iwp / (area * Es) #Settlement caused by the load at pile point
		Se3 = ( (Qs/fos) * size * (1- mu_s**2) * Iws) / (perimeter * L * Es)   #settlement caused by the load transmitted along the pile shaft

		S = np.round((Se1 + Se2 + Se3)*1000, 5)   #total pile settlement in mm

		print('\n' + '~'*125 + '\nRESULTS\n' + '~'*125)
		print('\n\nUltimate Bearing Load Capacity : ' + str(Qup) + ' kN')
		print('Allowable Bearing Load Capacity : ' + str(Qap) + ' kN')
		print('Total pile settlement : ' + str(S) + ' mm')
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		#DATAFRAME CREATION
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		if method == 1 :
			layers = ['Loose sand', 'Dense sand', 'Clayey']
			
			var = ['BEARING LOAD CAPACITY OF PILE', '', 'STATIC ANALYSIS', 'INPUT', 'Pile type', 'Shape', 'Side' if shape==1 else 'Radius','Elastic modulus of pile material', 'Angle of internal friction for last layer',
				   'Modulus of Elasticity of soil at or below the pile point', 'Poisson\'s ratio of soil','FOS', 'Number of layers', 
				   'Soil Info', 'Layer type', 'Unit weight', 'Angle of internal friction', 'depth of layers', 'Adhesion factor', 'cohesion', 
				   'Depth of water table', 'Nature of skin friction resistance distribution along the pile shaft',
				   '', 'COMPUTED VALUES', 'Area of pile tip', 'perimeter of pile tip', 'Surface area of pile in each layer', 
				   'Depth of layer considered (taking into account the critical depth)', 'End bearing resistance', 'Skin resistance for each layer', '',
				   'RESULTS', 'Ultimate Bearing Load Capacity', 'Allowable Bearing Load Capacity', 'Total pile settlement']
			val = ['', '','', '', 'Driven' if pile_type==1 else 'Bored', 'Square' if shape==1 else 'Circular', size,Ep, phi_last,Es, mu_s,fos, n_layers, 
			       '', [layers[i-1] for i in layer_type], gamma_t, phi, h1, alpha, cu, 
			       wt,'Uniform or Parabolic' if dist_type == 1 else 'Triangular', '', '', area, perimeter, sai, h, Qb, qi,'', '', Qup, Qap, S]
			units = ['','', '', '', '', '', 'm','kN/m^2', 'deg','kN/m^2','', '', '', 
			         '', '','kN/m^3', 'deg', 'm', '', 'kN/m^2', 
			         'm', '', '', '', 'm^2','m', 'm^2', 'm', 'kN', 'kN','', '', 'kN', 'kN', 'mm']

		else :
			var = ['BEARING LOAD CAPACITY OF PILE', '', 'USE OF SPT VALUES', 'INPUT', 'Pile type', 'Shape', 'Side' if shape==1 else 'Radius',
				   'Elastic modulus of pile material', 'Modulus of Elasticity of soil at or below the pile point', 'Poisson\'s ratio of soil',
				   'Average N value at pile tip', 'Average N along the pile shaft', 'Factor of Safety', 'COMPUTED VALUES',
				   'Cross-sectional area of pile tip', 'Surface area of pile shaft', 'End bearing resistance', 'Skin friction resistance',
				   'RESULTS', 'Ultimate Bearing Load Capacity', 'Allowable Bearing Load Capacity', 'Total pile settlement']
			val = ['', '', '', '','Bored', 'Square' if shape==1 else 'Circular', size, Ep, Es, mu_s, N, N_bar, fos, '', area, surface_area, Qb, Qs, 
				   '', Qup, Qap, S]
			units = ['','', '', '','', '', 'm','kN/m^2','kN/m^2','', '', '', '', '', 'm^2', 'm^2', 'kN', 'kN', '', 'kN', 'kN', 'mm']

		df = pd.DataFrame({'Description' : var, 'Values' : val, 'Unit' : units})
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		#REPORT CREATION
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		a = input('\nDo you want to print report in .csv/.xlsx format?(Y/N) ')
		if a.lower() == 'n' :
			print('Printing report cancelled...')
			time.sleep(1.5)
			main_screen()
		else :
			file_name = input('File name : ')
			ext = re.findall(r'\.(.+)', file_name)
			if ext != [] and ext[0] == 'csv' :
				df.to_csv(file_name, index=False)
			else :
				file_name = file_name + '.xlsx'
				df.to_excel(file_name, index=False)
			
			_here = os.path.dirname(os.path.abspath(__file__))
			report_path = os.path.join(_here, file_name)
			
			#Any notes for the report
			comments = input("Note: ")	
			report_index(file_name, report_path, comments)                 #Updating the report_index file
			
			print ('\nReport saved at ' + report_path + '  ' + '\U0001F44D')
			print('~'*100)
			_ = input('Press Enter to go back ')
			main_screen()

	except ValueError :
		print('\n\n\tOoops. You encountered a value error.' + '\U0001F926' + '\tEnter values again.')
		time.sleep(1.5)
		clear_screen()
		computation()

	except :
		print('\n\n\tOoops. Something went wrong.' + '\U0001F926' + '\tEnter values again.')
		time.sleep(1.5)
		clear_screen()
		computation()


def show_report() :
	'''for showing the report record in the program'''
	_here = os.path.dirname(os.path.abspath(__file__))
	filename = os.path.join(_here, 'report_index.csv')
	
	data = pd.read_csv(filename)
	print('~'*150 + '\n\t\t\tREPORT INDEX ' +  '\U0001F4D4'+ '\n' + '~'*150)
	print('\n')
	print('Program run : ', data['Values'][0])

	df_new = pd.DataFrame({'Report_Name' : [], 'Path' : [], 'Timestamp' : [], 'Comment' : []})
	for i in range(data.shape[0]-4) :
		if os.path.isfile(data['Values'][i+4]) :  #if the file exists i.e. it is not deleted or moved
			temp = pd.DataFrame({'Report_Name' : [data['Description'][i+4]], 'Path' : [data['Values'][i+4]], 
			                     'Timestamp' : [data['Timestamp'][i+4]], 'Comment' : [data['Comment'][i+4]]})
			df_new = df_new.append(temp)

	print('Reports saved : ', df_new.shape[0])
	print('\n')

	if df_new.shape[0] > 0 :
		table = Table(df_new.values)   #use of the table class written below
		print(table) 
	
	_ = input('\n\nPress Enter to go back  ')
	main_screen()


def main_screen() :            #home screen
	clear_screen()
	try : 
		choice = int(input('~'*150 + '\n\t\t\tPILES  ' +  '\N{construction worker}' + '\n' + '~'*150 +  '\n\n\t1. Find bearing load capacity \n\n\t2. Report Index\n\n\t3. Instructions \n\n\t4. About Devs\n\n\t5. Quit\n\n\n\tEnter : '))
	except ValueError :
		print('\n\n\tOoops. You encountered a value error.' + '\U0001F926' + '\tEnter values again.')
		time.sleep(1.5)
		main_screen()

	except :
		print('\n\n\tOoops. Something went wrong.' + '\U0001F926' + '\tEnter values again.')
		time.sleep(1.5)
		main_screen()

	if choice == 5 :
		print('\n\nProgram closing....Peace ' + '\U0001F596')
		time.sleep(1)
		clear_screen()
		sys.exit() 	#exit the program

	elif choice not in [1,2,3,4] :
		print('\nNot an option right now. Please enter again. ')
		time.sleep(1.5)
		main_screen()
		
	clear_screen()
	if choice == 1 :
		computation()
	elif choice == 2 :
		show_report()
	elif choice == 3 :
		instructions()
	else :
		about_us()


#This is the tough part. Wrapping multiline text in a table is hard and no library offers that directly. 

class Table:

    def __init__(self, contents, wrap=35, colDelim = "|", rowDelim = "-"):
        self.contents = contents
        self.wrap = wrap
        self.colDelim = colDelim

        # Extra rowDelim characters where colDelim characters are
        p = len(self.colDelim) * (len(self.contents[0]) - 1)

        # Line gets too long for one concatenation
        self.rowDelim = self.colDelim
        self.rowDelim += rowDelim * (self.wrap * max([len(i) for i in self.contents]) + p)
        self.rowDelim += self.colDelim + "\n"

    def withTextWrap(self):

        string = self.rowDelim

        # Restructure to get textwrap.wrap output for each cell
        l = [[textwrap.wrap(col, self.wrap) for col in row] for row in self.contents]

        for row in l:
            for n in range(max([len(i) for i in row])):
                string += self.colDelim
                for col in row:
                    if n < len(col):
                        string += col[n].ljust(self.wrap)
                    else:
                        string += " " * self.wrap
                    string += self.colDelim
                string += "\n"
            string += self.rowDelim

        return string

    def __str__(self):
        return self.withTextWrap()



if __name__ == "__main__" :
	package_check()         #checking packages 
	
	import numpy as np
	import pandas as pd
	pd.set_option('mode.chained_assignment', None)
	import textwrap
	
	run_count()				#updating run counter
	main_screen()    		#displaying main screen
