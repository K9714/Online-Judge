/* 
   https://cafe.naver.com/gogoomas/382574
   네이버 카페 질문 알고리즘 작성
   
   * 문제

    1. 대소문자 구분없이 배열에 있는 중복단어 제거
    2. 단어 중 동일한 문구가 들어간 경우 제거 [인덱스가 빠른 거 기준으로 살립니다]
    ※동일한 문구는 2글자 이상인경우만 해당됩니다.
    [EX. 나룻배 나물무침 나랑드사이다 -> 나룻배 물무침 랑드사이다 (X)]

    1번
    입력 : 차량용스마트폰 가정집스마트폰 기업용스마트폰
    출력 : 차량용스마트폰 가정집 기업용

    2번
    입력 : A4 강아지고양이 장난감 고양이 a4
    출력 : A4 강아지고양이 장난감
*/
static void Main(string[] args)
{
    // 최초 주어지는 단어 배열
    string input = "A4 강아지고양이 장난감 고양이 a4";

    // 단어를 넣을 딕셔너리 생성
    Dictionary<string, int> dict = new Dictionary<string, int>();

    // 공백으로 문자열 분리
    string[] words = input.Split(' ');
    // 분리된 문자열 foreach 전개
    foreach(string word in words)
    {
        // 만약 해당 단어의 Key 가 없다면
        if (!dict.ContainsKey(word))
        {
            if (dict.Count > 0)
            {
                // 딕셔너리가 비어있지 않은 경우 중복 단어 검사 실행
                // 딕셔너리 키 전개
                string checkWord = "";
                bool check = false;
                string newWord = word;
                foreach (string key in dict.Keys)
                {
                    // 첫 글자부터 2글자+ 형태로 분리하여 순서대로 딕셔너리 키에 해당하는 글자가 있는지 검사
                    Console.WriteLine($"[{word} in {key}]");
                    for (int i = 0; i <= word.Length - 2; i++)
                    {
                        check = false;
                        // 길이를 늘려가며 검사
                        for (int length = 2; length <= word.Length - i; length++)
                        {
                            // word 
                            checkWord = word.Substring(i, length);
                            Console.WriteLine($"{checkWord}");
                            if (!key.Contains(checkWord))
                            {
                                if (length > 2)
                                    checkWord = word.Substring(i, length - 1);
                                else
                                    checkWord = "";
                                break;
                            }
                            else
                            {
                                // 한번이라도 겹치는 단어가 발견되면 체크
                                check = true;
                            }
                        }
                        // 겹치는 단어가 있는 경우 반복 중지
                        if (check)
                            break;
                    }
                    // 포함하는 단어 제거한 단어
                    if (checkWord.Length > 0)
                    {
                        newWord = word.Replace(checkWord, "");
                        break;
                    }
                    else
                        newWord = word;
                                
                }
                if (dict.ContainsKey(newWord))
                {
                    dict[newWord] += 1;
                }
                else if (newWord.Length > 0)
                {
                    dict.Add(newWord, 1);
                }
            }
            else
            {
                // 딕셔너리가 비어있는 경우 생성
                dict.Add(word, 1);
            }
        }
        else
        {
            // 존재하면 카운트만 진행
            dict[word] += 1;
        }
    }

    foreach(KeyValuePair<string, int> kv in dict)
    {
        Console.Write($"{kv.Key} ");
    }
    Console.ReadLine();
}
