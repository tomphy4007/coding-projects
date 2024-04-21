def gradient_color(start_color, end_color, text):
    num_lines = text.count("\n") + 1
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color

    
    r_step = (r2 - r1) / num_lines
    g_step = (g2 - g1) / num_lines
    b_step = (b2 - b1) / num_lines

    lines = text.split("\n")
    for i, line in enumerate(lines):
       
        r = int(r1 + (r_step * i))
        g = int(g1 + (g_step * i))
        b = int(b1 + (b_step * i))

       
        print(f"\033[38;2;{r};{g};{b}m{line}\033[0m")


start_color = (124, 252, 0)

end_color = (46, 139, 87)

text = """
                                 88                                     
                                 ""                                     
                                                                        
,adPPYba, 8b       d8 8b,dPPYba, 88 8b,dPPYba,   ,adPPYb,d8  ,adPPYba,  
I8[    "" `8b     d8' 88P'   "Y8 88 88P'   `"8a a8"    `Y88 a8P_____88  
 `"Y8ba,   `8b   d8'  88         88 88       88 8b       88 8PP"""""""  
aa    ]8I   `8b,d8'   88         88 88       88 "8a,   ,d88 "8b,   ,aa  
`"YbbdP"'     Y88'    88         88 88       88  `"YbbdP"Y8  `"Ybbd8"'  
              d8'                                aa,    ,88             
             d8'                                  "Y8bbdP"    
                                                                                      
"""

gradient_color(start_color, end_color, text)
