import matplotlib.pyplot as plt

class Stats():
    alphabet = []
    name = ""
    extension = ""
    chars_to_skip = [" ", ",", ".", "\n", "\t"]
    stat = {}
    
    def get_file_info(self):
        self.name=input("Enter file name: ")
        self.extension=input("Enter file extension (if there is no extension just press enter): ")
        if self.extension != "": self.name = self.name+"."+self.extension
        else: self.name = self.name+self.extension

    def get_alphabet(self):
        try:
            file = open(self.name, "r")
            text = file.read().lower()
            for c in text:
                if c not in self.alphabet and c not in self.chars_to_skip:
                    self.alphabet.append(c)

            self.alphabet.sort()
            
        except FileNotFoundError:
            print("File not found")
        except UnboundLocalError:
            print("There is reference to variable without any value")
        finally:
            try:
                file.close()
            except FileNotFoundError:
                print("File not found")
            except UnboundLocalError:
                print("There is reference to variable without any value")

    def read_file(self):
        try:
            file = open(self.name, "r")
            text = file.read()
            print("\n",34*"-","FILE", 34*"-")
            print(text)
            print(29*"-","THE END OF FILE",29*"-","\n")
            
        except FileNotFoundError:
            print("File not found")
        except UnboundLocalError:
            print("There is reference to variable without any value")
        finally:
            try:
                file.close()
            except FileNotFoundError:
                print("File not found")
            except UnboundLocalError:
                print("There is reference to variable without any value")

    def stats(self):
        try:
            file = open(self.name, "r")
            text = file.read().lower()
            for i in range(len(self.alphabet)):
                self.stat.update({self.alphabet[i]:0})
                
            for i in range(len(self.alphabet)):
                for c in text:
                    if c == self.alphabet[i]:
                        self.stat[c] += 1
                        
        except FileNotFoundError:
            print("File not found")
        except UnboundLocalError:
            print("There is reference to variable without any value")
        finally:
            try:
                file.close()
            except FileNotFoundError:
                print("File not found")
            except UnboundLocalError:
                print("There is reference to variable without any value5")

    def print_statistics(self):
        print(31*"*"+" STATISTICS "+31*"*")
        summary = 0
		
        for it in self.stat.keys():
            print(it,"->",self.stat[it])
			
        for it in self.stat.keys():
            summary += self.stat[it]

        print(f"\nNumber of all characters (except characters to skip {self.chars_to_skip}: {summary}")
		
        print("\n",25*"*"+" THE END OF STATISTICS "+25*"*")

    def make_chart(self):
        chart = plt.figure(num=f"Chart for {self.name}")
        chart = plt.plot(self.stat.keys(), self.stat.values(), ".")
        chart = plt.xlabel("Characters from the given alphabet")
        chart = plt.ylabel("Number of characters")
        plt.show()

s = Stats()
s.get_file_info()
s.get_alphabet()
s.read_file()
s.stats()
s.print_statistics()
s.make_chart()
