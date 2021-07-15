**1. Set-up project**
  - git clone https://github.com/hunglthe150135/MAS_PROJECT.git
  - cd .\MAS_PROJECT\
  - git checkout -b _ngohieu_
  - git push --set-upstream origin _ngohieu_
  - _git branch_: kiểm tra mình đang ở branch nào trước khi code.

**2. Kéo code**
  - git stash
  - git pull origin hunglt
  - git stash apply 
  - _Nếu có conflict, tự resolve conflict. Sau đó git add ._

**3. Đẩy code**
  - Kéo code
  - git add .
  - git commit -m "_lời nhắn nào đó_"
  - git push
  - **Lập tức** nhắn tin cho mình là đã push, mình sẽ kéo branch của mọi người về. Không cần tạo pull request. Phải đảm bảo không có conflict trước khi push.

**4. Merge code**
  - Đẩy code
  - git checkout hunglt
  - git pull origin _tên_nhánh_
  - Đẩy code
