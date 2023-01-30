import requests
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
print("Status code:",r.status_code)
files=r.json()
print(files.keys())
print("total repositories:",files["total_count"])
print(len(files["items"]))
a=files["items"]
file=a[0]
print("Keys:",len(file))
for key in sorted(file):
    print(key)

    with open("统计.txt","w",encoding="utf-8") as f:
        for x in a:    
            f.write("\nName:"+str(x["name"]))
            f.write("\nOwner:"+str(x["owner"]["login"]))
            f.write("\nStars:"+str(x["stargazers_count"]))
            f.write("\nRepository:"+str(x["html_url"]))
            f.write("\nDescription:"+str(x["description"]))