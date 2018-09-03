# for finding the second highest number 
n = int(input())
m_list = []
for i in range(n):
    m_list.append(int(input()))

m_list.remove(max(m_list))
print(list(filter((2).__ne__, m_list)))
print('\n',m_list)
print(max(m_list))