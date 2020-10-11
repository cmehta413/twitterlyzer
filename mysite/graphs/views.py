from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
import pandas as pd



def home(request):
	

	


	dataS = pd.read_csv("/Users/chiragmehta/Downloads/archive/Project6500.csv", encoding= 'unicode_escape')




	plt.hist(dataS['sentiment'])
	plt.xlabel('Sentiment')
	plt.ylabel('Frequency')

	fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri =  urllib.parse.quote(string)
	return render(request,'home.html',{'data':uri})
	
	
# Create your views here.
