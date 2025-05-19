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
  %".2" = load i32, i32* @"a"
  %".3" = icmp ne i32 %".2", 0
  br i1 %".3", label %"if.then", label %"if.else"
if.then:
  store i32 1, i32* @"b"
  br label %"if.end"
if.else:
  store i32 2, i32* @"b"
  br label %"if.end"
if.end:
  %".9" = load i32, i32* @"b"
  %".10" = bitcast [3 x i8]* @".str.8341731685562686835" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".9")
  %".12" = bitcast [2 x i8]* @".str.4313221362129951564" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  ret void
}

@"a" = common global i32 0
@"b" = common global i32 0