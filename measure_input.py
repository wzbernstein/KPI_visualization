from IPython.display import HTML

input_form = """
<div style="background-color:gainsboro; border:solid black; width:300px; padding:20px;">
  <span id="PDOT">PDOT</span> : <input type="text" id="PDOT_value" value=""><br>
  <span id="PRI">PRI</span> : <input type="text" id="PRI_value" value=""><br>
  <span id="PUST">PUST</span> : <input type="text" id="PUST_value" value=""><br>
  <span id="AUST">AUST</span> : <input type="text" id="AUST_value" value=""><br>
  <span id="APT">APT</span> : <input type="text" id="APT_value" value=""><br>
  <span id="ADOT">ADOT</span> : <input type="text" id="ADOT_value" value=""><br>
  <span id="ATT">ATT</span> : <input type="text" id="ATT_value" value=""><br>
  <span id="AQT">AQT</span> : <input type="text" id="AQT_value" value=""><br>
  <span id="APWT">APWT</span> : <input type="text" id="APWT_value" value=""><br>
  <span id="APAT">APAT</span> : <input type="text" id="APAT_value" value=""><br>
  <span id="GQ">GQ</span> : <input type="text" id="GQ_value" value=""><br>
  <span id="SQ">SQ</span> : <input type="text" id="SQ_value" value=""><br>
  <span id="PSQ">PSQ</span> : <input type="text" id="PSQ_value" value=""><br>
  <span id="RQ">RQ</span> : <input type="text" id="RQ_value" value=""><br>
  <span id="OTBF">OTBF</span> : <input type="text" id="OTBF_value" value=""><br>
  <span id="CMT">CMT</span> : <input type="text" id="CMT_value" value=""><br>
  <span id="PMT">PMT</span> : <input type="text" id="PMT_value" value=""><br>
  <span id="BLT">BLT</span> : <input type="text" id="BLT_value" value=""><br>  
  <span id="STT">STT</span> : <input type="text" id="STT_value" value=""><br>  
<button onclick="set_value()">Set Value</button>
</div>
"""

javascript = """
<script type="text/Javascript">
    function set_value(){
        
        var PDOT = document.getElementById('PDOT').innerHTML; 
        var PDOT_value = document.getElementById('PDOT_value').value;            
        var command_PDOT = PDOT + " = '" + PDOT_value + "'";
        console.log("Executing Command: " + command_PDOT);
        
        var PRI = document.getElementById('PRI').innerHTML; 
        var PRI_value = document.getElementById('PRI_value').value;            
        var command_PRI = PRI + " = '" + PRI_value + "'";
        console.log("Executing Command: " + command_PRI);
        
        var PUST = document.getElementById('PUST').innerHTML; 
        var PUST_value = document.getElementById('PUST_value').value;            
        var command_PUST = PUST + " = '" + PUST_value + "'";
        console.log("Executing Command: " + command_PUST);

        var AUST = document.getElementById('AUST').innerHTML; 
        var AUST_value = document.getElementById('AUST_value').value;            
        var command_AUST = AUST + " = '" + AUST_value + "'";
        console.log("Executing Command: " + command_AUST);
        
        var APT = document.getElementById('APT').innerHTML; 
        var APT_value = document.getElementById('APT_value').value;            
        var command_APT = APT + " = '" + APT_value + "'";
        console.log("Executing Command: " + command_APT);
        
        var ADOT = document.getElementById('ADOT').innerHTML; 
        var ADOT_value = document.getElementById('ADOT_value').value;            
        var command_ADOT = ADOT + " = '" + ADOT_value + "'";
        console.log("Executing Command: " + command_ADOT);
        
        var ATT = document.getElementById('ATT').innerHTML; 
        var ATT_value = document.getElementById('ATT_value').value;            
        var command_ATT = ATT + " = '" + ATT_value + "'";
        console.log("Executing Command: " + command_ATT);
        
        var AQT = document.getElementById('AQT').innerHTML; 
        var AQT_value = document.getElementById('AQT_value').value;            
        var command_AQT = AQT + " = '" + AQT_value + "'";
        console.log("Executing Command: " + command_AQT);
        
                var APWT = document.getElementById('APWT').innerHTML; 
        var APWT_value = document.getElementById('APWT_value').value;            
        var command_APWT = APWT + " = '" + APWT_value + "'";
        console.log("Executing Command: " + command_APWT);
        
                var APAT = document.getElementById('APAT').innerHTML; 
        var APAT_value = document.getElementById('APAT_value').value;            
        var command_APAT = APAT + " = '" + APAT_value + "'";
        console.log("Executing Command: " + command_APAT);
        
                var GQ = document.getElementById('GQ').innerHTML; 
        var GQ_value = document.getElementById('GQ_value').value;            
        var command_GQ = GQ + " = '" + GQ_value + "'";
        console.log("Executing Command: " + command_GQ);
        
                        var SQ = document.getElementById('SQ').innerHTML; 
        var SQ_value = document.getElementById('SQ_value').value;            
        var command_SQ = SQ + " = '" + SQ_value + "'";
        console.log("Executing Command: " + command_SQ);

        var PSQ = document.getElementById('PSQ').innerHTML; 
        var PSQ_value = document.getElementById('PSQ_value').value;            
        var command_PSQ = PSQ + " = '" + PSQ_value + "'";
        console.log("Executing Command: " + command_PSQ);

        var RQ = document.getElementById('RQ').innerHTML; 
        var RQ_value = document.getElementById('RQ_value').value;            
        var command_RQ = RQ + " = '" + RQ_value + "'";
        console.log("Executing Command: " + command_RQ);
        
        var OTBF = document.getElementById('OTBF').innerHTML; 
        var OTBF_value = document.getElementById('OTBF_value').value;            
        var command_OTBF = OTBF + " = '" + OTBF_value + "'";
        console.log("Executing Command: " + command_OTBF);

        var CMT = document.getElementById('CMT').innerHTML; 
        var CMT_value = document.getElementById('CMT_value').value;            
        var command_CMT = CMT + " = '" + CMT_value + "'";
        console.log("Executing Command: " + command_CMT);

        var PMT = document.getElementById('PMT').innerHTML; 
        var PMT_value = document.getElementById('PMT_value').value;            
        var command_PMT = PMT + " = '" + PMT_value + "'";
        console.log("Executing Command: " + command_PMT);
        
        var BLT = document.getElementById('BLT').innerHTML; 
        var BLT_value = document.getElementById('BLT_value').value;            
        var command_BLT = BLT + " = '" + BLT_value + "'";
        console.log("Executing Command: " + command_BLT);
        
        var STT = document.getElementById('STT').innerHTML; 
        var STT_value = document.getElementById('STT_value').value;            
        var command_STT = STT + " = '" + STT_value + "'";
        console.log("Executing Command: " + command_STT);
        
        var kernel = IPython.notebook.kernel;
        kernel.execute(command_PDOT);
        kernel.execute(command_PRI);
        kernel.execute(command_PUST);
        kernel.execute(command_AUST);
        kernel.execute(command_APT);
        kernel.execute(command_ADOT);
        kernel.execute(command_ATT);
        kernel.execute(command_AQT);
        kernel.execute(command_APWT);
        kernel.execute(command_APAT);
        kernel.execute(command_GQ);
        kernel.execute(command_SQ);
        kernel.execute(command_PSQ);
        kernel.execute(command_RQ);
        kernel.execute(command_OTBF);
        kernel.execute(command_CMT);
        kernel.execute(command_PMT);
        kernel.execute(command_BLT);
        kernel.execute(command_STT);
    }
</script>
"""
HTML(input_form + javascript)