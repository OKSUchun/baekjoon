n = int(input())
end_num = 1
way = 1

while n > end_num:
    end_num += 6* way
    way +=1
print(way)
