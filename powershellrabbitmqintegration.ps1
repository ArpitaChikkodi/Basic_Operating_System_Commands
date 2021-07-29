$port = 4000
try{
	$endpoint = New-Object System.Net.IPEndPoint([IPAddress]::Any, $port)
	$tcplistener = New-Object System.Net.Sockets.TcpListener $endpoint
    $tcplistener.Start()
    Write-Host "TCP Server started" -fore Cyan

        #check queue here
        Write-Host "Checking if any new messages are in the queue..." -fore Cyan
        
        
            Import-Module D:\Setups\RabbitMQTools -force
            Get-RabbitMQConnection "amqp://testuser:testuser@192.168.29.233:5672/%2f"
            $QueueName = "test11"
            
            $ct = Get-RabbitMQMessage -VirtualHost / -Name $QueueName 
            $no_of_messages = $ct.message_count
            if ($no_of_messages -eq $null)
            {
                Write-Host "Queue is empty"
            }
            else {
                
            $no_of_messages = $no_of_messages + 1   #It starts count from 0
            Write-Host "Total number of messages in the queue are : "$no_of_messages
            $Incoming = Get-RabbitMQMessage -VirtualHost / -Name $QueueName -count $no_of_messages -Remove
            $IncomingData = $Incoming.payload | ConvertFrom-Json
            Write-Host $IncomingData
            }
}
catch{
	throw $_
	exit -1}
do{
Write-Host "Listening..(checking for client connections)"
$client = $tcplistener.AcceptTcpClient()
Write-Host "Connected to client!!" -fore Cyan
$stream = $client.GetStream()
$reader = New-Object System.IO.StreamReader $stream
do{
    $line = $reader.ReadLine()
    Write-Host $line -fore Cyan
}while ($line -and $line -ne ([char]4))
    $reader.Dispose()
    $stream.Dispose()
    $client.Dispose()
    $userinput = Read-Host -Prompt 'Give input: '
    if ($userinput -eq 'q')
    {
        $tcplistener.Stop()
        exit
    }
    else {
        continue
    }
}while ($line -ne ([char]4))
$tcplistener.Stop()