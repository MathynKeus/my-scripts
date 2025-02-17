# Storing the Shellmons in a Hashtable
$Shellmon = @{
    "Pikashell" = @{
        HP = 100
        Attack = @{
            Name = "Thundershock"
            Damage = (Get-Random -Minimum 1 -Maximum 10)
        }
    }
    "Shellizard" = @{
        HP = 100
        Attack = @{
            Name = "Flamethrower"
            Damage = (Get-Random -Minimum 1 -Maximum 15)
        }
    }
    "Blastoshell" = @{
        HP = 100
        Attack = @{
            Name = "Hydro Pump"
            Damage = (Get-Random -Minimum 1 -Maximum 15)
        }
    }
    "Venushell" = @{
        HP = 100
        Attack = @{
            Name = "Solar Beam"
            Damage = (Get-Random -Minimum 1 -Maximum 15)
        }
    }
}

# Display all available Shellmons
Write-Host "Available Shellmons:"
foreach ($shellmonName in $Shellmon.Keys) {
    Write-Host "- $shellmonName"
}

# Player chooses a Shellmon
$playerChoice = Read-Host "Choose your Shellmon (Pikashell, Shellizard, Blastoshell, Venushell)"
$playerShellmon = $Shellmon[$playerChoice]

Write-Host " "
Write-Host "You choose for: " $playerChoice 
Write-Host " "

# Computer chooses a random Shellmon
$computerChoice = $Shellmon.Keys | Get-Random
$computerShellmon = $shellmon[$computerChoice]

Write-Host "The computer choose for: " $computerChoice
Write-Host " "
Write-Host "The computer choose for: " $computerChoice

