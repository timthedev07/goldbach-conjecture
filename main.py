def genPrimes(n):
  primes = []
  for i in range(1, n + 1):
    currIsPrime = True
    for j in range(2, i):
      if (i % j) == 0:
        currIsPrime = False
        break
    if currIsPrime:
      primes.append(i)
  return primes

def cachePrimes(n, primes):
  # caching key => n
  key = hexKey(n)
  with open("primes.txt", "w") as f:
    f.write(",".join([str(i) for i in primes]) + "," + key)

def hexKey(n):
  return f"n = {n}".encode("utf-8").hex()


def getPrimes(n):
  with open("primes.txt", "r") as f:
    raw = f.read()
    commaSeparated = raw.split(",")
    storedKey = commaSeparated[-1]
    if "\n" in storedKey:
      storedKey = storedKey.replace("\n", "")

    # if the keys stored indicates that the cache has a larger
    # number of primes than needed(n), just fetch from cache
    cachedN = int(bytes.fromhex(storedKey).decode('utf-8').replace("n = ", ""))
    if storedKey == hexKey(n) or cachedN > n:
      return [int(commaSeparated[i]) for i in range(0, min(len(commaSeparated), n) - 1)]
    else:
      primes = genPrimes(n)
      cachePrimes(n, primes)
      return primes

def primeSums(n, primes):
  """
  Params:
   - n = the number you want to find prime sums of
   - primes = all primes from 1 to n inclusive
  
  Note, the sum could be of two equal numbers(e.g. 2 + 2)
  """
  sums = []
  numPrimes = len(primes)

  for i in range(numPrimes):
    for j in range(i, numPrimes):
      if primes[i] + primes[j] == n:
        sums.append((primes[i], primes[j]))

  return sums

def displaySums(sums, n):
  for sum in sums:
    print(f"{n} = {sum[0]} + {sum[1]}")

def main():
  n = 1
  while True:
    try:
      n = int(input("n(even): "))
    except ValueError:
      print("n has to be even, try again")
      continue

    if n % 2 == 0:
      break
    print("n has to be even, try again")

  print()

  primes = getPrimes(n)
  sums = primeSums(n, primes)
  displaySums(sums, n)
  
if __name__ == "__main__":
  main()
