$room="chenyifaer"
#$room="71771"
$request_interval=100

function is_stream() {
    $url="http://www.douyutv.com/"+$room
    $reply=(New-Object System.Net.WebClient).DownloadString($url)
    $status = $reply.Contains("feedback_report_button")
    return $status
}

while($true){
Try {
    Write-Output("start monitoring streaming status of " + $room)
    if (is_stream) {
        Write-Output($room + ' started live streaming at '+ (Get-Date -format MMdd_HHmm))
        [System.Windows.Forms.MessageBox]::Show($room , $room)
        while (is_stream) {Start-Sleep -Seconds 3600}
        }
    Start-Sleep -Seconds $request_interval
 }
catch {
      Write-Warning "Error occured: $_"
    }
 }