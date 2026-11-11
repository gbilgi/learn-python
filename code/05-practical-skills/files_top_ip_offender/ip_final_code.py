import time
import re
from typing import Generator
from collections import Counter


ip_pattern: re.Pattern[str] = re.compile(r'(\d+\.\d+\.\d+\.\d+)')




def read_from_logs_gen(file_name: str, encoding: str = "utf-8", errors: str = "ignore") -> Generator[str, None, None]:
   with open(file_name, "r", encoding=encoding, errors=errors) as file:
       for line in file:
           yield line.strip()




def extract_ip_address(log_line: str) -> str:
   match = ip_pattern.search(log_line)
   return match.group(1) if match else ""




def count_ips(file_name: str) -> Counter:
   ip_counter: Counter = Counter()
   try:
       for line in read_from_logs_gen(file_name):
           ip = extract_ip_address(line)
           if ip:
               ip_counter[ip] += 1
   except FileNotFoundError:
       print(f"Error: The file '{file_name}' was not found. Check your path.")
       exit()
   except PermissionError:
       print(f"Error: You do not have read permission for '{file_name}'. Try running with sudo.")
       exit()
   except Exception as e:
       print(f"Error: An unexpected error occurred: {e}")
       exit()


   return ip_counter




def print_summary(ip_counter: Counter) -> None:
   print("\n--- Summary ---")
   print(f"  Total Unique IPs : {len(ip_counter)}")
   print(f"  Total Requests   : {sum(ip_counter.values())}")




def print_top_ips(ip_counter: Counter, top_n: int = 5) -> None:
   print(f"\n--- Top {top_n} Troublemaker IPs ---")
   top_ips = ip_counter.most_common(top_n)
   for ip, count in top_ips:
       print(f"  {ip}: {count} requests")




def main(log_file: str = "app.logs", top_n: int = 5) -> None:
   start_time = time.time()


   ip_counter = count_ips(log_file)
   print_summary(ip_counter)
   print_top_ips(ip_counter, top_n)


   elapsed_time = time.time() - start_time
   print(f"\n  Time taken: {elapsed_time:.2f} seconds")




if __name__ == "__main__":
   main()


