def fixedPayment(bal,annualIr, months):
    monthlyIr = annualIr /12
    minimumFmp = int(bal/12)
    updatedBem = bal
    while minimumFmp % 10 != 0:
        minimumFmp += 1
    def processing(bal, minimumFmp, monthlyIr, months, updatedBem):
        while updatedBem > 0:
            for i in range(months):
                monthlyUb = updatedBem - minimumFmp
                updatedBem = monthlyUb * (monthlyIr + 1)
            if updatedBem > 0:
                updatedBem = bal
                minimumFmp += 10
            else: 
                break
        return minimumFmp
    minimumFmp = processing(bal, minimumFmp, monthlyIr, months, updatedBem)
    return minimumFmp
print(fixedPayment(3329, 0.2, 12))
