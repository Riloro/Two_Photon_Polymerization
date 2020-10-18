<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="19008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="clean.vi" Type="VI" URL="../clean.vi"/>
		<Item Name="controlPanel.vi" Type="VI" URL="../controlPanel.vi"/>
		<Item Name="GeneratePlaneEquation.vi" Type="VI" URL="../GeneratePlaneEquation.vi"/>
		<Item Name="main.vi" Type="VI" URL="../main.vi"/>
		<Item Name="newMain.vi" Type="VI" URL="../newMain.vi"/>
		<Item Name="RelativePos.vi" Type="VI" URL="../RelativePos.vi"/>
		<Item Name="Set3Points.vi" Type="VI" URL="../Set3Points.vi"/>
		<Item Name="setUp.vi" Type="VI" URL="../setUp.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="NI_Matrix.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/Matrix/NI_Matrix.lvlib"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
			</Item>
			<Item Name="#5.vi" Type="VI" URL="../../Low Level/Special command.llb/#5.vi"/>
			<Item Name="#5_old.vi" Type="VI" URL="../../Low Level/Old commands.llb/#5_old.vi"/>
			<Item Name="#7.vi" Type="VI" URL="../../Low Level/Special command.llb/#7.vi"/>
			<Item Name="#9.vi" Type="VI" URL="../../Low Level/WaveGenerator.llb/#9.vi"/>
			<Item Name="#24.vi" Type="VI" URL="../../Low Level/Special command.llb/#24.vi"/>
			<Item Name="*IDN?.vi" Type="VI" URL="../../Low Level/General command.llb/*IDN?.vi"/>
			<Item Name="Analog FGlobal.vi" Type="VI" URL="../../Low Level/Analog control.llb/Analog FGlobal.vi"/>
			<Item Name="Analog Functions.vi" Type="VI" URL="../../Low Level/Analog control.llb/Analog Functions.vi"/>
			<Item Name="Analog Receive String.vi" Type="VI" URL="../../Low Level/Analog control.llb/Analog Receive String.vi"/>
			<Item Name="Assign booleans from string to axes.vi" Type="VI" URL="../../Low Level/Support.llb/Assign booleans from string to axes.vi"/>
			<Item Name="Assign values from string to axes.vi" Type="VI" URL="../../Low Level/Support.llb/Assign values from string to axes.vi"/>
			<Item Name="ATZ.vi" Type="VI" URL="../../Low Level/Limits.llb/ATZ.vi"/>
			<Item Name="ATZ?.vi" Type="VI" URL="../../Low Level/Limits.llb/ATZ?.vi"/>
			<Item Name="Available Analog Commands.ctl" Type="VI" URL="../../Low Level/Analog control.llb/Available Analog Commands.ctl"/>
			<Item Name="Available DLL interfaces.ctl" Type="VI" URL="../../Low Level/Communication.llb/Available DLL interfaces.ctl"/>
			<Item Name="Available DLLs.ctl" Type="VI" URL="../../Low Level/Communication.llb/Available DLLs.ctl"/>
			<Item Name="Available interfaces.ctl" Type="VI" URL="../../Low Level/Communication.llb/Available interfaces.ctl"/>
			<Item Name="Build command substring.vi" Type="VI" URL="../../Low Level/Support.llb/Build command substring.vi"/>
			<Item Name="Build query command substring.vi" Type="VI" URL="../../Low Level/Support.llb/Build query command substring.vi"/>
			<Item Name="Close connection if open.vi" Type="VI" URL="../../Low Level/Communication.llb/Close connection if open.vi"/>
			<Item Name="Commanded axes connected?.vi" Type="VI" URL="../../Low Level/Support.llb/Commanded axes connected?.vi"/>
			<Item Name="Controller names.ctl" Type="VI" URL="../../Low Level/General command.llb/Controller names.ctl"/>
			<Item Name="CST?.vi" Type="VI" URL="../../Low Level/Special command.llb/CST?.vi"/>
			<Item Name="Cut out additional spaces.vi" Type="VI" URL="../../Low Level/Support.llb/Cut out additional spaces.vi"/>
			<Item Name="Define axes to command from boolean array.vi" Type="VI" URL="../../Low Level/Support.llb/Define axes to command from boolean array.vi"/>
			<Item Name="Define connected axes.vi" Type="VI" URL="../../Low Level/General command.llb/Define connected axes.vi"/>
			<Item Name="Define connected systems (Array).vi" Type="VI" URL="../../Low Level/General command.llb/Define connected systems (Array).vi"/>
			<Item Name="E727_Configuration_Setup.vi" Type="VI" URL="../../E727_Configuration_Setup.vi"/>
			<Item Name="ERR?.vi" Type="VI" URL="../../Low Level/General command.llb/ERR?.vi"/>
			<Item Name="Find host address.vi" Type="VI" URL="../../Low Level/Communication.llb/Find host address.vi"/>
			<Item Name="GCSTranslateError.vi" Type="VI" URL="../../Low Level/Support.llb/GCSTranslateError.vi"/>
			<Item Name="GCSTranslator DLL Functions.vi" Type="VI" URL="../../Low Level/Communication.llb/GCSTranslator DLL Functions.vi"/>
			<Item Name="GCSTranslator.dll" Type="Document" URL="../../../../PI_LabVIEW_Merge_Tool/DLL_Versions/GCSTranslator_win64/GCSTranslator.dll"/>
			<Item Name="General wait for movement to stop.vi" Type="VI" URL="../../Low Level/Support.llb/General wait for movement to stop.vi"/>
			<Item Name="Get all axes.vi" Type="VI" URL="../../Low Level/Support.llb/Get all axes.vi"/>
			<Item Name="Get arrays without blanks.vi" Type="VI" URL="../../Low Level/Support.llb/Get arrays without blanks.vi"/>
			<Item Name="Get lines from string.vi" Type="VI" URL="../../Low Level/Support.llb/Get lines from string.vi"/>
			<Item Name="Get subnet.vi" Type="VI" URL="../../Low Level/Communication.llb/Get subnet.vi"/>
			<Item Name="Global Analog.vi" Type="VI" URL="../../Low Level/Analog control.llb/Global Analog.vi"/>
			<Item Name="Global DaisyChain.vi" Type="VI" URL="../../Low Level/Communication.llb/Global DaisyChain.vi"/>
			<Item Name="Global1.vi" Type="VI" URL="../../Low Level/Communication.llb/Global1.vi"/>
			<Item Name="Global2 (Array).vi" Type="VI" URL="../../Low Level/General command.llb/Global2 (Array).vi"/>
			<Item Name="Initialize Global DaisyChain.vi" Type="VI" URL="../../Low Level/Communication.llb/Initialize Global DaisyChain.vi"/>
			<Item Name="Initialize Global1.vi" Type="VI" URL="../../Low Level/Communication.llb/Initialize Global1.vi"/>
			<Item Name="Initialize Global2.vi" Type="VI" URL="../../Low Level/General command.llb/Initialize Global2.vi"/>
			<Item Name="Is DaisyChain open.vi" Type="VI" URL="../../Low Level/Communication.llb/Is DaisyChain open.vi"/>
			<Item Name="Longlasting one-axis command.vi" Type="VI" URL="../../Low Level/Support.llb/Longlasting one-axis command.vi"/>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="MOV.vi" Type="VI" URL="../../Low Level/General command.llb/MOV.vi"/>
			<Item Name="MVR.vi" Type="VI" URL="../../Low Level/General command.llb/MVR.vi"/>
			<Item Name="ONT?.vi" Type="VI" URL="../../Low Level/General command.llb/ONT?.vi"/>
			<Item Name="PI Open Interface of one system.vi" Type="VI" URL="../../Low Level/Communication.llb/PI Open Interface of one system.vi"/>
			<Item Name="PI Receive String.vi" Type="VI" URL="../../Low Level/Communication.llb/PI Receive String.vi"/>
			<Item Name="PI Send String.vi" Type="VI" URL="../../Low Level/Communication.llb/PI Send String.vi"/>
			<Item Name="PI VISA Receive Characters.vi" Type="VI" URL="../../Low Level/Communication.llb/PI VISA Receive Characters.vi"/>
			<Item Name="POS?.vi" Type="VI" URL="../../Low Level/General command.llb/POS?.vi"/>
			<Item Name="Return space.vi" Type="VI" URL="../../Low Level/Support.llb/Return space.vi"/>
			<Item Name="SAI?.vi" Type="VI" URL="../../Low Level/General command.llb/SAI?.vi"/>
			<Item Name="Select host address.vi" Type="VI" URL="../../Low Level/Communication.llb/Select host address.vi"/>
			<Item Name="Select USB device.vi" Type="VI" URL="../../Low Level/Communication.llb/Select USB device.vi"/>
			<Item Name="Select values for chosen axes.vi" Type="VI" URL="../../Low Level/Support.llb/Select values for chosen axes.vi"/>
			<Item Name="SetUpE727.vi" Type="VI" URL="../SetUpE727.vi"/>
			<Item Name="STA?.vi" Type="VI" URL="../../Low Level/Special command.llb/STA?.vi"/>
			<Item Name="String with ASCII code conversion.vi" Type="VI" URL="../../Low Level/Support.llb/String with ASCII code conversion.vi"/>
			<Item Name="Substract axes array subset from axes array.vi" Type="VI" URL="../../Low Level/Support.llb/Substract axes array subset from axes array.vi"/>
			<Item Name="SVO.vi" Type="VI" URL="../../Low Level/General command.llb/SVO.vi"/>
			<Item Name="SVO?.vi" Type="VI" URL="../../Low Level/General command.llb/SVO?.vi"/>
			<Item Name="Termination character.ctl" Type="VI" URL="../../Low Level/Communication.llb/Termination character.ctl"/>
			<Item Name="TMN?.vi" Type="VI" URL="../../Low Level/Limits.llb/TMN?.vi"/>
			<Item Name="TMX?.vi" Type="VI" URL="../../Low Level/Limits.llb/TMX?.vi"/>
			<Item Name="TWG?.vi" Type="VI" URL="../../Low Level/WaveGenerator.llb/TWG?.vi"/>
			<Item Name="Wait for answer of longlasting command.vi" Type="VI" URL="../../Low Level/Support.llb/Wait for answer of longlasting command.vi"/>
			<Item Name="Wait for axes to stop.vi" Type="VI" URL="../../Low Level/Support.llb/Wait for axes to stop.vi"/>
			<Item Name="Wait for hexapod system axes to stop.vi" Type="VI" URL="../../Low Level/Old commands.llb/Wait for hexapod system axes to stop.vi"/>
			<Item Name="WGO.vi" Type="VI" URL="../../Low Level/WaveGenerator.llb/WGO.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
