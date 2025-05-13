; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.8372795069725211921" = internal constant [3 x i8] c"%d\00"
@".str.170774002489608625" = internal constant [3 x i8] c"%f\00"
@".str.3693790085204977514" = internal constant [3 x i8] c"%s\00"
@".str.332649807079450794" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %".3" = load i32, i32* %"a"
  %".4" = icmp ne i32 %".3", 0
  %".5" = xor i1 %".4", 1
  %".6" = zext i1 %".5" to i32
  %"b" = alloca i32
  store i32 %".6", i32* %"b"
  %".8" = load i32, i32* %"b"
  %".9" = bitcast [2 x i8]* @".str.332649807079450794" to i8*
  %".10" = bitcast [3 x i8]* @".str.8372795069725211921" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".8")
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".9")
  ret void
}
