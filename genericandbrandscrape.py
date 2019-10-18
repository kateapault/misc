urls = [
  'https://www.drugs.com/condition/depression.html?category_id=&include_rx=true&show_off_label=true&only_generics=true&submitted=true',
  'https://www.drugs.com/condition/depression.html?category_id=&include_rx=true&show_off_label=true&only_generics=true&submitted=true&page_number=2',
  'https://www.drugs.com/condition/depression.html?category_id=&include_rx=true&show_off_label=true&only_generics=true&submitted=true&page_number=3'
]
for url in urls:
  drugspagehtml = requests.get(url,headers=headers)
  dpage = BeautifulSoup(drugspagehtml.content,'html.parser')

  generics = dpage.find_all('a',{'class':"condition-table__drug-name__link"})

  genericslist = []
  for i in range(len(generics)):
      genericslist.append(generics[i].get_text().capitalize())

  drugs = dpage.find_all('tr',{'class':"condition-profile"})
  medicationlist = []
  for i in range(len(genericslist)):
      brands = drugs[i].find_all('span',{'class':'condition-table__brand-names__brand-name'})
      brandnames = '('
      for brand in brands:
          brandnames += (noSpace(brand.get_text()) + ' ')
      brandnames += ')'

      medication = genericslist[i] + ' ' + brandnames
      medicationlist.append(medication)
  fileopen = open('depressionmeds.txt','a')
  for line in medicationlist:
      fileopen.write(line + '\n')
  fileopen.close()
