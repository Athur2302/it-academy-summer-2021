ужин_recipe = '' '<html> <body> <table>
<tr><th>amt</th><th>unit</th><th>item</th> </tr>
<tr><td>24</td><td> кусочки</td><td>багетта</td> </tr>
<tr><td>2+</td><td>tbsp</td> <td> оливковое масло </td> </tr>
<tr><td>1</td><td> кубок</td><td> помидоры</td> </tr>
<tr><td>1</td><td>jar</td><td>pesto</td> </tr>
</table></body> </html> '' '

импортировать xml.etree.ElementTree как etree
дерево = etree.fromstring (обед_рецепт)

кладовая = набор (['оливковое масло', 'песто'])
для ингредиента в tree.getiterator ('tr'):
    amt, unit, item = ингредиент
    если item.tag == "td" и item.text не в кладовой:
        print ("% s:% s% s"% (item.text, amt.text, unit.text))