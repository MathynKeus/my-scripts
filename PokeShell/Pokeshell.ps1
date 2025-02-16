#Making a Hashtable with the Shellmons
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




