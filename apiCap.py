# api testing tool gui in python
from tkinter import *
import tkinter.messagebox as tmsg
import customtkinter
import sys
import requests
import json

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = Tk()

root.title("ApiCap")
root.wm_iconbitmap("api.ico")
# Width X Height
root.geometry("567x787")

# width,height
root.minsize(800,800)

# width,height
root.maxsize(800,800)

# logic functions
def about():
	tmsg.showinfo("What is this software","This is a api testing tools which allows you to do request get,post,put,patch and delete without using browser.")

def httpUrl(url):
	if not url.startswith(("https://","http://")):
		return "http://"+url
	else:
		return url

def getRequest(url,headerInp,result,statusvar,sbar):
	url = httpUrl(url.get())
	headers = headerInp.get("1.0",END)
	if(len(url)!=0):
		try:
			if(len(headers)==10):
				headers = eval(headers)
				get = requests.get(url, headers=headers)
			else:
				get = requests.get(url)
			statusvar.set(get)
			sbar.update()  		
			content_type = get.headers.get('content-type')
			if 'application/json' in content_type:
				pretty_json = json.loads(get.text)
				result.delete("1.0", "end")
				val = json.dumps(pretty_json, indent=2)
				result.insert("1.0", val)
			else:
				result.delete("1.0", "end")
				val = get.text
				result.insert("1.0", val)
		except requests.exceptions.RequestException as e:
			result.delete("1.0", "end")
			result.insert("1.0", f"ERROR: {e}")
		except requests.exceptions.InvalidURL as e:
			result.delete("1.0", "end")
			result.insert("1.0", f"ERROR: {e}")


def postRequest(url,headerInp,result,dataInp,statusvar,sbar):
	url = url.get()
	headers = headerInp.get("1.0",END)
	execute = True
	try:
		dataInp = eval(dataInp.get("1.0",END))
	except Exception as e:
		execute = False
		error = "Enter DATA or URL properly wthout any mistakes."
		result.delete("1.0", "end")
		result.insert("1.0", f"ERROR: {error}")

	if(execute):
		if(len(url)!=0):
			try:
				if(len(headers)==10):
					headers = eval(headers)
					get = requests.post(url, headers=headers, json=dataInp)
				else:
					get = requests.post(url,json=dataInp)
				statusvar.set(get)
				sbar.update()
				content_type = get.headers.get('content-type')
				if 'application/json' in content_type:
					pretty_json = json.loads(get.text)
					result.delete("1.0", "end")
					val = json.dumps(pretty_json, indent=2)
					result.insert("1.0", val)
		
			except requests.exceptions.RequestException as e:
				result.delete("1.0", "end")
				result.insert("1.0", f"ERROR: {e}")
			except requests.exceptions.InvalidURL as e:
				result.delete("1.0", "end")
				result.insert("1.0", f"ERROR: {e}")

    
def putRequest(url,headerInp,result,dataInp,statusvar,sbar):
	url = url.get()
	headers = headerInp.get("1.0",END)
	execute = True
	try:
		dataInp = eval(dataInp.get("1.0",END))
	except Exception as e:
		execute = False
		error = "Enter DATA or URL properly wthout any mistakes."
		result.delete("1.0", "end")
		result.insert("1.0", f"ERROR: {error}")

	if(execute):
		if(len(url)!=0):
			try:
				if(len(headers)==10):
					headers = eval(headers)
					get = requests.put(url, headers=headers, json=dataInp)
				else:
					get = requests.put(url,json=dataInp)
				statusvar.set(get)
				sbar.update()
				content_type = get.headers.get('content-type')
				if 'application/json' in content_type:
					pretty_json = json.loads(get.text)
					result.delete("1.0", "end")
					val = json.dumps(pretty_json, indent=2)
					result.insert("1.0", val)

			except requests.exceptions.RequestException as e:
				result.delete("1.0", "end")
				result.insert("1.0", f"ERROR: {e}")
			except requests.exceptions.InvalidURL as e:
				result.delete("1.0", "end")
				result.insert("1.0", f"ERROR: {e}")

def patchRequest(url,headerInp,result,dataInp,statusvar,sbar):
	url = url.get()
	headers = headerInp.get("1.0",END)
	execute = True
	try:
		dataInp = eval(dataInp.get("1.0",END))
	except Exception as e:
		execute = False
		error = "Enter DATA or URL properly wthout any mistakes."
		result.delete("1.0", "end")
		result.insert("1.0", f"ERROR: {error}")

	if(execute):
		if(len(url)!=0):
			try:
				if(len(headers)==10):
					headers = eval(headers)
					get = requests.patch(url, headers=headers, json=dataInp)
				else:
					get = requests.patch(url,json=dataInp)
				statusvar.set(get)
				sbar.update()
				content_type = get.headers.get('content-type')
				if 'application/json' in content_type:
					pretty_json = json.loads(get.text)
					result.delete("1.0", "end")
					val = json.dumps(pretty_json, indent=2)
					result.insert("1.0", val)

			except requests.exceptions.RequestException as e:
				result.delete("1.0", "end")
				result.insert("1.0", f"ERROR: {e}")
			except requests.exceptions.InvalidURL as e:
				result.delete("1.0", "end")
				result.insert("1.0", f"ERROR: {e}")

def deleteRequest(url,headerInp,result,statusvar,sbar):
	url = url.get()
	headers = headerInp.get("1.0",END)
	if(len(url)!=0):
		try:
			if(len(headers)==10):
				headers = eval(headers)
				get = requests.delete(url, headers=headers)
			else:
				get = requests.delete(url)
			statusvar.set(get)
			sbar.update()
			content_type = get.headers.get('content-type')
			if 'application/json' in content_type:
				pretty_json = json.loads(get.text)
				result.delete("1.0", "end")
				val = json.dumps(pretty_json, indent=2)
				result.insert("1.0", val)
			else:
				result.delete("1.0", "end")
				result.insert("1.0", get.text)
		except requests.exceptions.RequestException as e:
			result.delete("1.0", "end")
			result.insert("1.0", f"ERROR: {e}")
		except requests.exceptions.InvalidURL as e:
			result.delete("1.0", "end")
			result.insert("1.0", f"ERROR: {e}")

def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

# frame container
container = Frame(root)
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

def show_frame(frame):
    frame.tkraise()

def create_frame():
    new_frame = customtkinter.CTkFrame(master=container)
    new_frame.grid(row=0, column=0, sticky="nsew")
    return new_frame
    
# Frames functions
def home():
	home = create_frame()
	mode = customtkinter.CTkOptionMenu(home, values=[ "Dark","Light", "System"],command=change_appearance_mode_event)
	mode.place(x=4,y=4)
	head = customtkinter.CTkLabel(master=home,text="What is an Api",font=customtkinter.CTkFont(size=40, weight="bold"))
	head.pack(pady=40)

	head_content = customtkinter.CTkLabel(master=home,text="""API stands for Application Programming Interface. It's a set of instructions\n and protocols written in programming languages that determine how two software\n components communicate with each other. APIs are like contracts that define how\n two software systems interact.""",font=customtkinter.CTkFont(size=15, weight="bold"))
	head_content.pack(pady=8,padx=20)

	req = customtkinter.CTkLabel(master=home,text="Types of REQUESTS you can do (Allowed).",font=customtkinter.CTkFont(size=20, weight="bold"))
	req.pack(pady=30)

	getReq = customtkinter.CTkLabel(master=home,text="1. {GET} : Requests data from a specified resource. GET requests can only retrieve data and\n should have no other effect on the server.",font=customtkinter.CTkFont(size=15, weight="bold"))
	getReq.pack(pady=10)

	postReq = customtkinter.CTkLabel(master=home,text="2. {POST} : Submits data to be processed to a specified resource. POST requests can send \ndata to the server, which can then process that data or store it.",font=customtkinter.CTkFont(size=15, weight="bold"))
	postReq.pack(pady=10)

	putReq = customtkinter.CTkLabel(master=home,text="3. {PUT} : Updates a resource or creates a new resource if it does not exist. PUT requests\t\ntypically require the client to specify the entire resource, not just the parts that are being changed.",font=customtkinter.CTkFont(size=15, weight="bold"))
	putReq.pack(pady=10)

	patchReq = customtkinter.CTkLabel(master=home,text="4. {PATCH} : Applies partial modifications to a resource. Unlike PUT, which typically replaces\n the entire resource, PATCH requests only update the parts of the resource that are specified in\n the request.",font=customtkinter.CTkFont(size=15, weight="bold"))
	patchReq.pack(pady=10)

	deleteReq = customtkinter.CTkLabel(master=home,text="5. {DELETE} : Deletes a specified resource.\t\t\t\t\t",font=customtkinter.CTkFont(size=15, weight="bold"))
	deleteReq.pack(pady=10)

	getBtn = customtkinter.CTkButton(master=home, text="GET", command=get)
	getBtn.pack(side=LEFT, padx=10)

	postBtn = customtkinter.CTkButton(master=home, text="POST", command=post)
	postBtn.pack(side=LEFT, padx=10)

	putBtn = customtkinter.CTkButton(master=home, text="PUT", command=put)
	putBtn.pack(side=LEFT, padx=10)

	patchBtn = customtkinter.CTkButton(master=home, text="PATCH", command=patch)
	patchBtn.pack(side=LEFT, padx=10)

	deleteBtn = customtkinter.CTkButton(master=home, text="DELETE", command=delete)
	deleteBtn.pack(side=LEFT, padx=10)


def get():
	# Get Page
	getFrame = create_frame()
	customtkinter.CTkLabel(getFrame,font=customtkinter.CTkFont(size=25, weight="bold"), text="Get Request",pady=20).pack(pady=10, padx=10)
	customtkinter.CTkLabel(getFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Enter Url").pack()
	url = StringVar()
	urlInp = customtkinter.CTkEntry(master=getFrame, textvariable=url,font=customtkinter.CTkFont(size=15)) 
	urlInp.pack(ipadx = 300, ipady=3)

	customtkinter.CTkLabel(getFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Headers (Optional)",pady=30).pack()
	headerInp = customtkinter.CTkTextbox(master=getFrame,font=customtkinter.CTkFont(size=15), width=410, height=160)
	headerInp.place(x=200,y=204) 

	customtkinter.CTkButton(master=getFrame,text="Request",command=lambda :getRequest(url,headerInp,result,statusvar,sbar)).pack(pady=180)
	
	customtkinter.CTkLabel(getFrame,font=customtkinter.CTkFont(size=12, weight="bold"), text="Results (wait after request)").place(x=200,y=450)
	result = customtkinter.CTkTextbox(master=getFrame,font=customtkinter.CTkFont(size=15), width=800, height=330)
	result.place(x=0,y=480)

	statusvar = StringVar()
	statusvar.set("Ready")
	sbar = customtkinter.CTkLabel(getFrame,font=customtkinter.CTkFont(size=12, weight="bold"), textvariable=statusvar)
	sbar.place(x=0,y=447)

def post():
	# Post
	postFrame = create_frame()
	customtkinter.CTkLabel(postFrame,font=customtkinter.CTkFont(size=25, weight="bold"), text="Post Request",pady=20).pack(pady=10, padx=10)
	customtkinter.CTkLabel(postFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Enter Url").pack()
	url = StringVar()
	urlInp = customtkinter.CTkEntry(master=postFrame, textvariable=url,font=customtkinter.CTkFont(size=15)) 
	urlInp.pack(ipadx = 300, ipady = 2)

	customtkinter.CTkLabel(postFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Headers (Optional)",pady=30).place(x=15,y=150)
	headerInp = customtkinter.CTkTextbox(master=postFrame, width=370, height=160)
	headerInp.place(x=15,y=204) 

	customtkinter.CTkLabel(postFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Data",pady=30).place(x=410,y=150)
	dataInp = customtkinter.CTkTextbox(master=postFrame,font=customtkinter.CTkFont(size=15), width=370, height=160)
	dataInp.place(x=410,y=204) 

	customtkinter.CTkButton(master=postFrame,text="Request",command=lambda :postRequest(url,headerInp,result,dataInp,statusvar,sbar)).pack(pady=260)

	customtkinter.CTkLabel(postFrame,font=customtkinter.CTkFont(size=12, weight="bold"), text="Results (wait after request)").place(x=200,y=450)
	result = customtkinter.CTkTextbox(master=postFrame,font=customtkinter.CTkFont(size=15), width=800, height=330)
	result.place(x=0,y=480)	

	statusvar = StringVar()
	statusvar.set("Ready")
	sbar = customtkinter.CTkLabel(postFrame,font=customtkinter.CTkFont(size=12, weight="bold"), textvariable=statusvar)
	sbar.place(x=0,y=447)


def put():
	# put 
	putFrame = create_frame()
	customtkinter.CTkLabel(master=putFrame,font=customtkinter.CTkFont(size=25, weight="bold"), text="Put Request",pady=20).pack(pady=10, padx=10)
	customtkinter.CTkLabel(master=putFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Enter Url").pack()
	url = StringVar()
	urlInp = customtkinter.CTkEntry(master=putFrame, textvariable=url,font=customtkinter.CTkFont(size=15)) 
	urlInp.pack(ipadx = 300, ipady = 2)

	customtkinter.CTkLabel(master=putFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Headers (Optional)",pady=30).place(x=15,y=150)
	headerInp = customtkinter.CTkTextbox(master=putFrame, width=370, height=160)
	headerInp.place(x=15,y=204) 

	customtkinter.CTkLabel(master=putFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Data",pady=30).place(x=410,y=150)
	dataInp = customtkinter.CTkTextbox(master=putFrame,font=customtkinter.CTkFont(size=15), width=370, height=160)
	dataInp.place(x=410,y=204) 

	customtkinter.CTkButton(master=putFrame,text="Request",command=lambda :putRequest(url,headerInp,result,dataInp,statusvar,sbar)).pack(pady=260)

	customtkinter.CTkLabel(master=putFrame,font=customtkinter.CTkFont(size=12, weight="bold"), text="Results (wait after request)").place(x=200,y=450)
	result = customtkinter.CTkTextbox(master=putFrame,font=customtkinter.CTkFont(size=15), width=800, height=330)
	result.place(x=0,y=480)	

	statusvar = StringVar()
	statusvar.set("Ready")
	sbar = customtkinter.CTkLabel(master=putFrame,font=customtkinter.CTkFont(size=12, weight="bold"), textvariable=statusvar)
	sbar.place(x=0,y=447)


def patch():
	# patch
	patchFrame = create_frame()
	customtkinter.CTkLabel(master=patchFrame,font=customtkinter.CTkFont(size=25, weight="bold"), text="Patch Request",pady=20).pack(pady=10, padx=10)
	customtkinter.CTkLabel(master=patchFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Enter Url").pack()
	url = StringVar()
	urlInp = customtkinter.CTkEntry(master=patchFrame, textvariable=url,font=customtkinter.CTkFont(size=15)) 
	urlInp.pack(ipadx = 300, ipady = 2)

	customtkinter.CTkLabel(master=patchFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Headers (Optional)",pady=30).place(x=15,y=150)
	headerInp = customtkinter.CTkTextbox(master=patchFrame, width=370, height=160)
	headerInp.place(x=15,y=204) 

	customtkinter.CTkLabel(master=patchFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Data",pady=30).place(x=410,y=150)
	dataInp = customtkinter.CTkTextbox(master=patchFrame,font=customtkinter.CTkFont(size=15), width=370, height=160)
	dataInp.place(x=410,y=204) 

	customtkinter.CTkButton(master=patchFrame,text="Request",command=lambda :patchRequest(url,headerInp,result,dataInp,statusvar,sbar)).pack(pady=260)

	customtkinter.CTkLabel(master=patchFrame,font=customtkinter.CTkFont(size=12, weight="bold"), text="Results (wait after request)").place(x=200,y=450)
	result = customtkinter.CTkTextbox(master=patchFrame,font=customtkinter.CTkFont(size=15), width=800, height=330)
	result.place(x=0,y=480)	

	statusvar = StringVar()
	statusvar.set("Ready")
	sbar = customtkinter.CTkLabel(master=patchFrame,font=customtkinter.CTkFont(size=12, weight="bold"), textvariable=statusvar)
	sbar.place(x=0,y=447)


def delete():
	# delete
	deleteFrame = create_frame()
	customtkinter.CTkLabel(master=deleteFrame,font=customtkinter.CTkFont(size=25, weight="bold"), text="Delete Request",pady=20).pack(pady=10, padx=10)
	customtkinter.CTkLabel(master=deleteFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Enter Url").pack()
	url = StringVar()
	urlInp = customtkinter.CTkEntry(master=deleteFrame, textvariable=url,font=customtkinter.CTkFont(size=15)) 
	urlInp.pack(ipadx = 300, ipady=3)

	customtkinter.CTkLabel(master=deleteFrame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Headers (Optional)",pady=30).pack()
	headerInp = customtkinter.CTkTextbox(master=deleteFrame,font=customtkinter.CTkFont(size=15), width=410, height=160)
	headerInp.place(x=200,y=204	,) 

	customtkinter.CTkButton(master=deleteFrame,text="Request",command=lambda :deleteRequest(url,headerInp,result,statusvar,sbar)).pack(pady=180)
	
	customtkinter.CTkLabel(master=deleteFrame,font=customtkinter.CTkFont(size=12, weight="bold"), text="Results (wait after request)").place(x=200,y=450)
	result = customtkinter.CTkTextbox(master=deleteFrame,font=customtkinter.CTkFont(size=15), width=800, height=330)
	result.place(x=0,y=480)

	statusvar = StringVar()
	statusvar.set("Ready")
	sbar = customtkinter.CTkLabel(master=deleteFrame,font=customtkinter.CTkFont(size=12, weight="bold"), textvariable=statusvar)
	sbar.place(x=0,y=447)



# menus
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Get", command=get)
m1.add_command(label="Post", command=post)
m1.add_command(label="Put", command=put)
m1.add_command(label="Patch", command=patch)
m1.add_command(label="Delete", command=delete)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Requests', menu=m1)

mainmenu.add_command(label="Home", command=home)
root.config(menu=mainmenu)

mainmenu.add_command(label="About", command=about)
root.config(menu=mainmenu)

mainmenu.add_command(label="Exit", command=lambda:sys.exit())
root.config(menu=mainmenu)

root.config(menu=mainmenu)

if __name__ == '__main__':
	home()
	root.mainloop()