 #Convert bytes into KB, MB and GB.

# Taking input from the user
bytes= float(input("Enter size in bytes: "))
kilobytes =bytes/ 1024
megabytes = kilobytes / 1024
gigabytes = megabytes / 1024

 # Displaying the results
print("Entered size in bytes : ",bytes,)
print(" Total size in kilobytes (KB) : ",kilobytes, "KB")
print(" Total size in megabytes (MB) : ",megabytes, "MB")
print(" Total size in gigabytes (GB) : ",gigabytes, "GB")
   