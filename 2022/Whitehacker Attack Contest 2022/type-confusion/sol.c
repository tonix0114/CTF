/*
type-confusion

- int64 입력 값을 double로 형변환 했을때 변환 값이 동일한 값을 찾는 문제입니다.
- int64 범위안에 값을 브루트포싱하면서 규칙을 찾아낸 결과 오차 범위를 줄여나갈 수 있는 값을 방법을 발견하였고 손으로 값을 바꿔가며 동일한 값을 찾아냈습니다.
- `WACon{Typ3-c0nFusion-w3akneSses_have-r3c3iv3d_sOme-a77entIon=by-app1ied_r3search3rs_and+maj0r_software+vendors_for_C__and-C++?code.}`

Xion님 풀이 (z3, angr)
https://discord.com/channels/989594598613581834/990585958867009576/990607698754142259

*/
#include <stdio.h>
#include <memory.h>

void main()
{
    for (__int64 i = 0x43d0f43d0f43d0f4;; i++)
    {
        __int64 input = i;
        double d_data = i;
        if (!memcmp(&input, &d_data, 8))
        {
            printf("%llx %llx\n", input, d_data);
        }
    }
}
```
