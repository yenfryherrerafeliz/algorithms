class LicenseKeyFormatter:
    def __init__(self, licenseKey):
        self.licenseKey = licenseKey.upper()
        
    
    def reformatLicenseKey(self, k):
        #first we count all the chars excluding dashes
        newLicenseKey = []
        
        chars_count = 0
        for c in self.licenseKey:
            if c != '-':
                chars_count += 1

        #then lets define how many chars will be in our first group
        items_by_group = chars_count % k
        item_count = 0
        
        for char_idx in range(len(self.licenseKey)):

            #Skip the dash char
            if self.licenseKey[char_idx] == '-':
                continue
            
            #condition to add a dash every items_by_group chars.
            #With this condition we prevent from adding a dash at the end of the new key.
            if item_count == items_by_group:

                #we this we prevent from adding a dash at the beginning of the new key
                if items_by_group != 0 and item_count != 0:
                    newLicenseKey.append('-')

                items_by_group = k    
                item_count = 0

            #add the current char to our new licenseKey
            elm = self.licenseKey[char_idx]
            newLicenseKey.append(elm)

            item_count += 1
            
        return ''.join(c for c in newLicenseKey)

    

if __name__ == '__main__':

    tests = [
        {'input': {'licenseKey': '5F3Z-2e-9-w', 'k': 4}, 'expected': '5F3Z-2E9W'},
        {'input': {'licenseKey': '2-5g-3-J', 'k': 2}, 'expected': '2-5G-3J'},
    ]

    for test in tests:
        licenseKey = test['input']['licenseKey']
        k = test['input']['k']
        formatter = LicenseKeyFormatter(licenseKey)
        formattedLicenseKey = formatter.reformatLicenseKey(k)

        print('Input: (licenseKey=', licenseKey, ', k=', k, ')', ', Output: ', formattedLicenseKey, ', Expected: ', test['expected'], ', Test passed: ', ('True' if test['expected'] == formattedLicenseKey else 'False'))
