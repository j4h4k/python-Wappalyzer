from Wappalyzer import Wappalyzer, WebPage

with open('/mnt/c/Users/demo/Desktop/wappalyzer_python/python-Wappalyzer/url.txt', 'r') as f:
	#data = f.read()
	#print (data)
	#for line in f:
	#lines = f.readlines()
	#i = 1
	for line in f:
		
		l=line.strip()
		webpage = WebPage.new_from_url(l)
		wappalyzer = Wappalyzer.latest()
		output = wappalyzer.analyze_with_versions_and_categories(webpage)
		print(output)

#thanks to pesa fs

#webpage = WebPage.new_from_url('https://skyrem.my')
#webpage = WebPage.new_from_url('http://157.230.253.55/wordpress/')
#webpage = WebPage.new_from_url('https://graduan.com/')
#wappalyzer = Wappalyzer.latest()
#wappalyzer = Wappalyzer.latest(update=True)
#print (wappalyzer.analyze(webpage))
#wappalyzer.analyze_with_versions_and_categories(webpage)
#output = wappalyzer.analyze_with_versions_and_categories(webpage)
#print(output)
