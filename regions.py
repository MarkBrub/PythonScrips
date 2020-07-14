import subprocess

#gets the list of regions and puts them in a list
subprocess = subprocess.run(["gcloud", "compute", "zones", "list"], stdout=subprocess.PIPE)
result = subprocess.stdout.decode('utf-8')
result = result.partition('\n')[2]

regions = result.splitlines()
for x in range(len(regions)):
    regions[x] = regions[x].partition(' ')[0]


#removes duplicate regions leaving only the first zone in each region
x = 0
while x != len(regions):
    for y in range(x + 1, len(regions)):
        if regions[x][:-1] == regions[y][:-1]:
            regions.pop(y)
            x -= 1
            break
    x += 1

#turns the list of regions into a comma seperated list
outString = ""
for r in regions:
    outString += r + ','

outString = outString[:-1] + '\n'


#puts the updated list on the end of the required lines
inFile = open("all_regions.yaml", 'r')
lines = inFile.readlines()
inFile.close()

for x, line in enumerate(lines):
    if "zones: " in line:
        lines[x] = line.partition(':')[0] + ": " + outString

outfile = open("all_regions.yaml", 'w')
for line in lines:
    outfile.write(line)
outfile.close()