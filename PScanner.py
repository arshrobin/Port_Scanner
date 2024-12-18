import socket
import argparse

def scan_port(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.connect((host, port))
    print(f"Port {port} is open")
  except:
    print(f"Port {port} is closed")
  finally:
    s.close()

def main():
  parser = argparse.ArgumentParser(description='Port Scanner')
  parser.add_argument('host', help='Target IP address')
  parser.add_argument('-p', '--ports', type=str, default='1-1024', help='Port range to scan (e.g., 1-1024, 22, 80, 443)')
  args = parser.parse_args()

  host = args.host
  port_range = args.ports

  start_port, end_port = map(int, port_range.split('-'))

  for port in range(start_port, end_port+1):
    scan_port(host, port)

if __name__ == "__main__":
  main()
