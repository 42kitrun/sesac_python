class DisplayData:
    def __init__(self, data):
        if isinstance(data, str):    # isinstance
            self.display_str(data)   # object가 classinfo의 인스턴스이면 True를 반환
        elif isinstance(data, list): # classinfo가 튜플인 경우, 
            self.display_list(data)  # object가 튜플 안에 있는 타입 중 하나라도 해당되면 True를 반환
        elif isinstance(data, dict):
            self.display_dict(data)
        else:
            raise TypeError("지원하지 않는 타입입니다.")
    
    def display_str(self, data):
        print(f"문자열: {data}")
        
    def display_list(self, data):
        print(f"리스트: {data}")
        
    def display_dict(self, data):
        print(f"딕셔너리: {data}")
        
    
DisplayData("hello")
DisplayData([1, 2, 3])
DisplayData({"a":1, "b":2})