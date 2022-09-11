def create_file_with_numbers(n):
    a= open(f'range_{n}.txt','a',encoding='utf-8')

    for i in range(1,n+1):
        a.write(f'{i}\n')
    a.close()

create_file_with_numbers(5)