import requests,json,time,math
import threading,datetime
response1_timelist = []
response2_timelist = []
thread_list = []
url = "http://surya-interview.appspot.com/message"


def find_std(num_list):
    list_sum = sum(num_list)
    list_mean = (list_sum*1.0)/len(num_list)
    diff_list = [ x-list_mean for x in num_list ]
    sq_diff_list = [ x**2 for x in diff_list ]
    sum_sq_diff_list = sum(sq_diff_list)
    variance = sum_sq_diff_list/len(num_list)
    std_num_list = math.sqrt(variance)
    return list_mean,std_num_list

def find_percentile(a,num_list):
    n = len(num_list)
    pos = (a/100.0)*n
    if pos == round(pos):
        pos = int(pos)
        return (num_list[pos-1]+num_list[pos])/2
    else:
        pos = int(round(pos-1))
        return num_list[pos]
def check_response():
    try:
		headers = {'X-Surya-Email-Id':'chinmay.m92@gmail.com'}
		request1_time1 = datetime.datetime.now()
		response = requests.get(url,headers = headers)
		if response.status_code >=400:
			raise Exception("Error code :%s, Message :%s " %(response.status_code,response.text))
		request1_time2 = datetime.datetime.now()
		request1_timedelta = request1_time2-request1_time1
		response1_timelist.append(request1_timedelta.total_seconds())
		data = response.json()
		request2_time1 = datetime.datetime.now()
		response = requests.post(url,data = json.dumps(headers))
		if response.status_code > 400:
			raise Exception("Error code :%s, Message :%s " %(response.status_code,response.text))
		request2_time2 = datetime.datetime.now()
		request2_timedelta = request2_time2-request2_time1
		response2_timelist.append(request2_timedelta.total_seconds())
    except Exception as e:
		print "Error occured while sending request. %s \n" %e
    
    
if __name__=="__main__":
    for i in range(100):
        t = threading.Thread(target=check_response)
        t.start()
        thread_list.append(t)
    for j in thread_list:
        while j.isAlive():
            j.join()
    if response1_timelist:
        response1_timelist.sort()
        print "Information for the first api"
        print "10 percentile",find_percentile(10,response1_timelist)
        print "50 percentile",find_percentile(50,response1_timelist)
        print "90 percentile",find_percentile(90,response1_timelist)
        print "95 percentile",find_percentile(95,response1_timelist)
        print "99 percentile",find_percentile(99,response1_timelist)
        mean,sd = find_std(response1_timelist)
        print "mean",mean
        print "standard deviation",sd
    else:
        print "No data for api1"
    print "*"*100
    if response2_timelist:
        response2_timelist.sort()
        print "Information for the second api"
        print "10 percentile",find_percentile(10,response2_timelist)
        print "50 percentile",find_percentile(50,response2_timelist)
        print "90 percentile",find_percentile(90,response2_timelist)
        print "95 percentile",find_percentile(95,response2_timelist)
        print "99 percentile",find_percentile(99,response2_timelist)
        mean,sd = find_std(response2_timelist)
        print "mean",mean
        print "standard deviation",sd
    else:
        print "No data for api2"


