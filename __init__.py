import re

def calculate(input : str):
  """
  Accepted operators and symbols:
    `^` or `**`: power

    `)` and `(`: brackets for computation ordering

    `+`: add

    `-`: subtract

    `x` or `*`: multiply

    `:` or `/`: divide

    `,` or `.`: decimal

  Args:
    input (str): input
  
  Raises:
    SyntaxError: When user inputs wrong syntax, i.e. Invalid brackets, Unsupported character, and Invalid operator

  Returns:
    number: result
  
  Examples:
    1+1*0

    3((5/(5/25))^(56/4))(5+6-(1+2+3+4))

    5(2)(4 --> Too many opening brackets

    5^^4 --> Operator error
    
    4/0 --> can't divide by zero!
  """  
  if re.search(r'[^0-9+\-*/:()Xx^.,\s]', input):
    raise SyntaxError('Accepts only numbers and symbols + - * x : / ) ( ^ . ,')
  input = (
    input
    .replace('++', '+')
      .replace('-+', '-')
        .replace('+-', '-')
          .replace('--', '+')
            .replace('^', '**')
              .replace('x', '*')
                .replace('X', '*')
                  .replace(':', '/')
                    .replace(',', '.')
                      .replace(' ', '')
  )
  op = input.count('(')
  cl = input.count(')')
  if op != cl:
    opcl = "opening" if op > cl else "closing"
    raise SyntaxError(f'There are too many {opcl} brackets somewhere')
  step1 = __validate__(input)
  # print('step 1:',step1)
  step2 = __calc__(step1.replace(' ', ''))
  # print('step 2:',step2)
  return step2

def __validate__(mth : str) -> str:
  # add missing * before ( or after )
  j = 1
  operators = ['+','-','*','/', '^']

  if len(mth.strip()) == 1:
    return mth

  while(True):
    if j == len(mth)-1:
      break
    if mth[j] == '(':
      if mth[j-1] not in operators and mth[j-1] != '(':
        # insert '*' at i
        mth = mth[:j] + '*' + mth[j:]
    elif mth[j] == ')':
      if mth[j+1] not in operators and mth[j+1] != ')':
        # insert '*' at i+1
        mth = mth[:j+1] + '*' + mth[j+1:]
    j+=1
  return mth

def __calc__(mth : str):
  tmp = ''
  final = ''
  unclosed = 0
  got_brace = False
  for n in mth:
    if n == '(':
      if got_brace:
        tmp += '('
      got_brace = True
      unclosed += 1
      continue
    if n == ')':
      unclosed -= 1
      if got_brace:
        if unclosed == 0:
          expanded = __calc__(tmp)
          final += expanded
          got_brace = False
          tmp = ''
        else:
          tmp += ')'
      continue
    if got_brace:
      tmp += n
    else:
      final += n
  
  result = str(eval(final))
  return result
