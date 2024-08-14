import html
import threading
import streamlit as st
import requests

st.balloons()

# streamlit run kcoj.py

id = st.text_input("start MSSV", "22110287")
id2 = st.text_input("end MSSV", "22110461")
mamon=st.text_input("Mã lớp học", 'WEPR330479_06')
vung=st.empty()

threads = []

lsthoten = []
def thread_function(name):
    url = "https://e-bills.vn/pay/hcmute?customer="+str(name)
    response = requests.get(url)
    if response.text.find(mamon)!=-1:
        info=response.text.split("\n")
        for i in info:
            if '<input type="text" class="form-control" id="hoten" value=' in i:
                hoten=i.split('value="')[1][0:-23:1]
                hoten = html.unescape(hoten)
                print(hoten)
                lsthoten.append(hoten)
                break


if st.button("Tra cứu"):
    for i in range(int(id),int(id2)+1):
        
        t = threading.Thread(target=thread_function, args=(i,))
        threads.append(t)
        t.start()
    # # await all threads to finish
    # for t in threads:
    #     t.join()
    #     with vung:
    #         st.write(f"Phần trăm hoàn thành: {round((i-int(id))/(int(id2)-int(id))*100,2)}%")
    #     if len(lsthoten) > 0:
    #         ht = lsthoten[-1]
    #         st.write('<h1 style="font-size:77px;color:purple;">'+ht+'</h1>',unsafe_allow_html=True)
    #         lsthoten.pop()
    for idx in range(len(threads)):
        with vung:
            st.write(f"Phần trăm hoàn thành: {(((idx+1)/len(threads))*100)}%")
        threads[idx].join()
        
        if len(lsthoten) > 0:
            ht = lsthoten[-1]
            st.write('<h1 style="font-size:77px;color:purple;">'+ht+'</h1>',unsafe_allow_html=True)
            lsthoten.pop()

        
