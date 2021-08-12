import cpuinfo, psutil

info = cpuinfo.get_cpu_info()
# print(type(info))
#
# for i in info:
#     print(i, ":", info[i])

print("Arquitetura:", info["arch"])
print("Processador:", info["brand_raw"])
print("Registradores:",info["bits"], "bits")
print("Número de núcleos:", psutil.cpu_count())
print("Número de núcleos físicos:", psutil.cpu_count(logical=False))
print("Frequência do processador:", round(psutil.cpu_freq().current/1024,2), "Ghz")

