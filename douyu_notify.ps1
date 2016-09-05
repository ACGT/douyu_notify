
$room="71771"
$request_interval=100

Add-Type -AssemblyName System.Windows.Forms

function is_stream() {
    $url="http://www.douyutv.com/"+$room
    $reply=(New-Object System.Net.WebClient).DownloadString($url)
    $status = $reply.Contains("feedback-report-button")
    return $status
}

Write-Output("start monitoring streaming status of " + $room)
while($true){
Try {
    if (is_stream) {
        Write-Output($room + ' started live streaming at '+ (Get-Date -format MMdd_HHmm))
        $oReturn=[System.Windows.Forms.MessageBox]::Show("press OK to launch "+$room,$room,[System.Windows.Forms.MessageBoxButtons]::OKCancel)	
        switch ($oReturn){
	        "OK" {
		        write-host "pressed OK"
                $url="http://www.douyutv.com/"+$room
		        start $url
	        } 
	        "Cancel" {
		        write-host "pressed Cancel"
		        # Enter some code
	        } 
        }
        while (is_stream) {Start-Sleep -Seconds 1800}
        }
    Start-Sleep -Seconds $request_interval
 }
catch {
      Write-Warning "Error occured: $_"
    }
 }
