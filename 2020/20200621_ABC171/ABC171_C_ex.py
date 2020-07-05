'''
参考:1
https://tanuhack.com/num2alpha-alpha2num/
数値からアルファベットの変換…10進数→26進数
-----
例えば、『1000』という数値をアルファベットに変換させる場合、
1. 26のn乗で1000以下の最大のnを求める→『n+1』がアルファベットの桁数、n=2
2. (26^2)*xで1000以下の最大のxを求める→x=1、つまり3桁目のアルファベットはA
3. (26^1)*yで1000-(26^2)*1=324以下の最大のyを求める→y=12、つまり2桁目のアルファベットはL
4. (26^0)*z=12→つまり3桁目のアルファベットはL、ゆえに1000はALL
と、再帰を使って算出
-----

参考:2
https://note.nkmk.me/python-chr-ord-unicode-code-point/
整数（Unicodeコードポイント）→文字
'''
def num2alpha(num):
    if num <= 26:                                   # num == 1, num == 2, ...etc
        return chr(96+num)                          # chr(97) == 'a'
    elif num % 26 == 0:                             # num == 26, num == 52, ...etc
        return num2alpha(num//26-1)+chr(122)        # chr(122) == 'z', ∴num == 52 ⇒ 'az'
    else:                                           # num == 27, num == 53, ...etc
        return num2alpha(num//26)+chr(96+num%26)    # ∴num == 53 ⇒ 'ba'


N = int(input())
ans = num2alpha(N)

print(ans)
