for _ in range(int(input())):
    n  =int(input())
    st = input()

    a = st.count("map")
    b = st.count("pie")
    c = st.count('mapie')

    print(a+b-c)

    