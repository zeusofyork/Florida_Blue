$cred = Get-Credential -UserName ""
$username = $cred.UserName
$password = $cred.Password

Write-Host "Welcome, $username!"

do {
    Write-Host ""
    Write-Host "Please select an option:"
    Write-Host "1. Option 1"
    Write-Host "2. Option 2"
    Write-Host "3. Option 3"
    Write-Host "4. Exit"
    $choice = Read-Host "Enter your choice"
    
    switch ($choice) {
        "1" {
            Write-Host "Option 1 submenu:"
            Write-Host "1. Sub-option 1"
            Write-Host "2. Sub-option 2"
            Write-Host "3. Sub-option 3"
            $subchoice = Read-Host "Enter your sub-choice"
            
            switch ($subchoice) {
                "1" {
                    Write-Host "You selected Option 1, Sub-option 1"
                }
                "2" {
                    Write-Host "You selected Option 1, Sub-option 2"
                }
                "3" {
                    Write-Host "You selected Option 1, Sub-option 3"
                }
                default {
                    Write-Host "Invalid sub-choice, please try again."
                }
            }
        }
        "2" {
            Write-Host "Option 2 submenu:"
            Write-Host "1. Sub-option 1"
            Write-Host "2. Sub-option 2"
            Write-Host "3. Sub-option 3"
            $subchoice = Read-Host "Enter your sub-choice"
            
            switch ($subchoice) {
                "1" {
                    Write-Host "You selected Option 2, Sub-option 1"
                }
                "2" {
                    Write-Host "You selected Option 2, Sub-option 2"
                }
                "3" {
                    Write-Host "You selected Option 2, Sub-option 3"
                }
                default {
                    Write-Host "Invalid sub-choice, please try again."
                }
            }
        }
        "3" {
            Write-Host "Option 3 submenu:"
            Write-Host "1. Sub-option 1"
            Write-Host "2. Sub-option 2"
            Write-Host "3. Sub-option 3"
            $subchoice = Read-Host "Enter your sub-choice"
            
            switch ($subchoice) {
                "1" {
                    Write-Host "You selected Option 3, Sub-option 1"
                }
                "2" {
                    Write-Host "You selected Option 3, Sub-option 2"
                }
                "3" {
                    Write-Host "You selected Option 3, Sub-option 3"
                }
                default {
                    Write-Host "Invalid sub-choice, please try again."
                }
            }
        }
        "4" {
            Write-Host "Exiting..."
        }
        default {
            Write-Host "Invalid choice, please try again."
        }
    }
} until ($choice -eq "4")
