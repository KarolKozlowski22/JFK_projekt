; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.8341731685562686835" = internal constant [3 x i8] c"%d\00"
@".str.8084496673346794580" = internal constant [3 x i8] c"%f\00"
@".str.8515177546619091338" = internal constant [3 x i8] c"%s\00"
@".str.4313221362129951564" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %".2" = call i32 @"add"(i32 3, i32 4)
  store i32 %".2", i32* @"result"
  %".4" = load i32, i32* @"result"
  %".5" = bitcast [3 x i8]* @".str.8341731685562686835" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".4")
  %".7" = bitcast [2 x i8]* @".str.4313221362129951564" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  ret void
}

@"result" = internal global i32 0
define i32 @"add"(i32 %"a", i32 %"b")
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %".6" = load i32, i32* %"a.1"
  %".7" = load i32, i32* %"b.1"
  %".8" = add i32 %".6", %".7"
  ret i32 %".8"
}
